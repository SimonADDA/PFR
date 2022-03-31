#AWS
import boto3
import json
import os

#PDFTEXT
import urllib.request
from pdfminer.high_level import extract_text

import re
path='./Download'
first_article=os.listdir(path)[0]
last_article=os.listdir(path)[-1]

# Load your PDF
def load_pdf(article):
    try:
        with open(f'Download/{article}', "rb") as f:
            text = extract_text(f)
            mypdftext=text
    except:
        with open(f'Professeur/{article}', "rb") as f:
            text = extract_text(f)
            mypdftext=text
    return mypdftext

pdf=load_pdf(first_article)

#First filter to have only the References from a pdf
def after_references(mypdftext=load_pdf(first_article)): 
    keyword1 = 'References'
    keyword2 = 'REFERENCES'
    keyword3 = 'R EFERENCES'
    keyword4 = 'Reference'

    if keyword1 in mypdftext :
            before_keyword, keyword, after_keyword = mypdftext.partition(keyword1)
    elif keyword2 in mypdftext :
            before_keyword, keyword, after_keyword = mypdftext.partition(keyword2)
    elif keyword3 in mypdftext :
            before_keyword, keyword, after_keyword = mypdftext.partition(keyword3)
    elif keyword4 in mypdftext :
            before_keyword, keyword, after_keyword = mypdftext.partition(keyword4)
    else:
        after_keyword = mypdftext[5000:]
    return after_keyword

    #Display references in the pdf
references=after_references(pdf)

#First cleaning of this text

replacement_patterns = [
    (r'won\'t', 'will not'),
    (r'can\'t', 'cannot'),
    (r'i\'m', 'i am'),
    (r'ain\'t', 'is not'),
    (r'(\w+)\'ll', '\g<1> will'),
    (r'(\w+)n\'t', '\g<1> not'),
    (r'(\w+)\'ve', '\g<1> have'),
    (r'(\w+)\'s', '\g<1> is'),
    (r'(\w+)\'re', '\g<1> are'),
    (r'(\w+)\'d', '\g<1> would'),
]

class RegexpReplacer(object):
    def __init__(self, patterns=replacement_patterns): 
        self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]
    def replace(self, text):
        s = text
        for (pattern, repl) in self.patterns:
            s = re.sub(pattern, repl, s) 
        return s

replacer=RegexpReplacer()
references=replacer.replace(references)


#Si erreur, ajoutez vos ID:
ACCESS_ID='...'
ACCESS_KEY='...'
session_token='...'

#With CLI
def compehend(references):
    try:
        comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
        input_text = references
        result_json=comprehend.detect_entities(Text=input_text, LanguageCode='en')
        print(result_json)
    except :
        comprehend = boto3.client(service_name='comprehend', region_name='us-east-1',aws_access_key_id=ACCESS_ID,
                                            aws_secret_access_key= ACCESS_KEY,aws_session_token=session_token)
        input_text = references
        result_json=comprehend.detect_entities(Text=input_text, LanguageCode='en')
        
    return result_json


result_json= compehend(references[:4000])

#Creation of json in order to keep only relevant information
def json_creation(result_json):
    output_json=[]
    i=0
    for json in result_json['Entities']:
        data={}
        if json['Type']== 'PERSON' and json['Score']>0.80:
            data["index"] = i
            data["Person"] = json['Text']
            data["Fiability"] = json['Score']
            output_json.append(data)
            i += 1
    return output_json


import json
import os

#Convert the array to json file
def create_json_file(jsonobject, filepath):
    with open(filepath, 'w') as outfile:
        json.dump(jsonobject, outfile)


#Import the json in my desktop
filename = "./AWS/Download/EntitiesPDF.json"
create_json_file(json_creation(result_json), filename)

#Display the json result
f = open("./AWS/Download/EntitiesPDF.json", "r")
print(f.read())