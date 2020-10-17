#Importing Libraries
import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

!pip3 install -U spacy

# NLP Component

import spacy
# import en_core_web_lg
# nlp = en_core_web_lg.load()

# Load the large English NLP model
nlp = spacy.load('en_core_web_sm')

# Replace a token with "REDACTED" if it is a name
def replace_name_with_placeholder(token):
  # if token part of speech is not an adjective and is a common word replace it
    if token.pos_ != "ADJ" and token.is_stop == True:
        return ""
    else:
        return token.string

# Loop through all the entities in a document and check if they are names
def scrub(text):
    doc = nlp(text)
    for ent in doc.ents:
        ent.merge()
    tokens = map(replace_name_with_placeholder, doc)
    return "".join(tokens)

s = """
In 1950, Alan Turing published his famous article "Computing Machinery and Intelligence". In 1957, Noam Chomsky’s 
Syntactic Structures revolutionized Linguistics with 'universal grammar', a rule based system of syntactic structures.
"""
print(scrub(s))
# doc = nlp(s)
