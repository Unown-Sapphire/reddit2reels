import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

with open("randompost.txt", "r", encoding="utf-8") as file:
    posts = file.read()
    
# Process whole documents
text = (posts)
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])