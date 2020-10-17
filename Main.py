**mPath Prototype**




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

# for token in doc:
#   print(token.pos_)


#Import from Google Sheet
from google.colab import auth
auth.authenticate_user()

import gspread
from oauth2client.client import GoogleCredentials

gc = gspread.authorize(GoogleCredentials.get_application_default())

worksheet = gc.open('Hackathon').sheet1
# THIS IS A MOCK DATABASE WITH ONLY 3/501 SYMPTOMS 

# get_all_values gives a list of rows.
rows = worksheet.get_all_values()
print(rows)

# Convert to a DataFrame and render.
import pandas as pd
pd.DataFrame.from_records(rows)



#Getting the user's input
patient_bio = []
patient_bio.append(input("What is your age: "))
gender = input("Please enter your biological gender (male or female)")
patient_bio.append(gender)
if gender == "Male" or "male" or "MALE":
  gender_value = 1
elif gender == "Female" or "female" or "FEMALE":
  gender_value = 0
symptom_name = input("Please enter symptoms: ")
symptom_list = symptom_name.split()
print(symptom_list)

from selenium import webdriver
from bs4 import BeautifulSoup
from threading import Thread
from urllib.request import urlopen 

def function(): 
    driver = webdriver.Chrome(r"C:\Users\maini\Downloads\chromedriver.exe")
    protocols = driver.get("https://app.cleartriage.com/app/#/protocols")

    # Requires a second URL because the website requires a sign-in, and the URL changes after the sign-in
    protocols2 = input("url: ")
    html = urlopen(protocols2).read()
    soup = BeautifulSoup(html, features="html.parser")    
    
    #kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    
        # get text
        text = soup.get_text()
    
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
    
        print(text)
        
function()

action_thread = Thread(target=function)
action_thread.start()
action_thread.join(timeout=15)
