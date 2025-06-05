import spacy
from spacy.lang.en.stop_words import STOP_WORDS

nlp=spacy.load("en_core_web_sm")

print(len(STOP_WORDS))

doc=nlp("We just opened our wings , the flying part is coming soon")
# for token in doc:
#     if token.is_stop:
#         print(token)

# def preprocessing(text):
#     doc=nlp(text)
#     no_stop_words=[token.text for token in doc if not token.is_stop and not token.is_punct]
#     return print(no_stop_words)

# preprocessing(doc)
# print(no_stop_words)


########################################

import pandas as pd

df=pd.read_json("combined.json",lines=True)
print(df)
print(df["title"])



   







