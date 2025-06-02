# nltk - is like a manual camera where we have to adjust everysetting to be a powerfull tool
# spacy - is like an iphone which have already adjusted values and hence provide easiness for clicking pictures


import spacy
import nltk
from nltk.tokenize import sent_tokenize

nlp = spacy.load("en_core_web_sm") 
# nlp = spacy.blank("en") #for English
# nlp = spacy.blank("ge") #for german
#Goto spacy language model on google too get more languages

# text = "Dr. Strange loves pav bhaji of mumbai as it costs only 2$ per plate"
# doc = nlp(text)
# print(sent_tokenize(text)) #nltk

# for sentence in doc.sents:  #for sentence breaking
#     print(sentence)

# for sentence in doc.sents:  #for word tokenisation
#     for words in sentence:
#         print(words)

with open("student.txt")as f:
    text=f.readlines()
# print(text)   #breaking text into array of lines

text=' '.join(text) #converting array to a single line
# doc=nlp(text)
# email=[]
# for token in doc:
#     if token.like_email:
#         email.append(token.text)
# print(email)                         #extracting only the email

nlp2=spacy.blank('hi')
doc2=nlp("क्ऐसे हो भैया,मेरे 500 उपय्य उधर दे दो !!")
for token in doc2:
    print(token,token.is_currency,token.like_num)


