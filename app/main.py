from operator import le
from re import A
from typing import Optional
from unittest import result
import uvicorn
import numpy
from fastapi import FastAPI
from pydoc import doc
import nltk
from nltk import word_tokenize,pos_tag
nltk.download("maxent_ne_chunker")
nltk.download("words")
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def NLTK_function_tag(text:str):
    tokens = word_tokenize(text)
    tag=pos_tag(tokens)
    yield tag

def NLTK_function_NER(quote):
    words = word_tokenize(quote)
    tags = nltk.pos_tag(words)
    tree = nltk.ne_chunk(tags, binary=True)
    return set(
        " ".join(i[0] for i in t)
        for t in tree
        if hasattr(t, "label") and t.label() == "NE"
    )

app = FastAPI(
    title=" API which extract entities with NLTK"
)

@app.get('/NLTK/Tag')
def my_text(text:str):
    output_spacy=list(NLTK_function_tag(text))
    result={"Tag in text from NLTK ": output_spacy}
    return result

@app.get('/NLTK/NER')
def my_text(text:str):
    output_spacy=list(NLTK_function_NER(text))
    result={"Names entities in text from NLTK ": output_spacy}
    return result
    