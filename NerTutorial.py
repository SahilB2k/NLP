# NER - Name Entiry Recognition
# extracting entities from a given text
# eg - ELon Musk:Person
# eg tesla:Organisation
# common use case - recommendation system

import spacy

nlp=spacy.load("en_core_web_sm")

print(nlp.pipe_names)
doc=nlp("Tesla Inc is going to acquire twitter for $45 billion")
for ent in doc.ents:
    print(ent.text,"|",ent.label_,"|",spacy.explain(ent.label_))