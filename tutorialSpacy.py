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
# print(email)                       #extracting only the email



# nlp2=spacy.blank('hi')
# doc2=nlp("क्ऐसे हो भैया,मेरे 500 उपय्य उधर दे दो !!")
# for token in doc2:
#     print(token,token.is_currency,token.like_num)

# from spacy.symbols import ORTH

# doc=nlp("gimme double cheese extra large healthy pizza")
# tokens=[token.text for token in doc] #priting tokens directly in array
# print(tokens)  


# nlp.tokenizer.add_special_case("gimme",[  #using ORTH lib to convert special words to their root/base words
#     {ORTH:"gim"},
#     {ORTH:"me"}
# ])

# doc2=nlp("gimme double cheese extra large healthy pizza")

# tokens=[token.text for token in doc2]
# print(tokens) #printing all the base words from the text


text='''
Look for data to help you address the question. Governments are good
sources because data from public research is often freely available. Good
places to start include http://www.data.gov/, and http://www.science.
gov/, and in the United Kingdom, http://data.gov.uk/.
Two of my favorite data sets are the General Social Survey at http://www3.norc.org/gss+website/, 
and the European Social Survey at http://www.europeansocialsurvey.org/.
'''

doc=nlp(text)
data_website=[token.text for token in doc if token.like_url]
print(data_website)

transactions = "Tony gave two $ to Peter, Bruce gave 500 € to Steve"
doc2=nlp(transactions)
for token in doc2:
    if token.like_num and doc2[token.i+1].is_currency:
        print(token,doc[token.i+1].text)