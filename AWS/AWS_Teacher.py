import re
from AWS_Exemple import load_pdf, compehend, json_creation, create_json_file

#AWS
import boto3
import json
import os

#PDFTEXT
import urllib.request
import pdftotext

import re
path='./AWS/Professeur'
article_teacher=os.listdir(path)[-1]
my_article=load_pdf(article_teacher)
my_article=my_article[:5000]

#AWS comprehend
result_json=compehend(my_article)

#Creation of json in order to keep only relevant information
import json
import os

#Import the json in my desktop
filename = "./AWS/Professeur/AWS_json_teacher.json"
create_json_file(json_creation(result_json), filename)

#Display the json result
f = open("./AWS/Professeur/AWS_json_teacher.json", "r")
print(f.read())