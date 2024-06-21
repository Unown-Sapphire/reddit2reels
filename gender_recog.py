import spacy

nlp = spacy.load("en_core_web_sm")

with open("randompost.txt", "r", encoding="uts-8") as file:
    lines = file.read()
