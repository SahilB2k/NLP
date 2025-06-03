import nltk
import spacy

nlp=spacy.load("en_core_web_sm")

with open("news_story.txt") as f:
    text=f.read()
    # print(text)
    
doc=nlp(text)

count=doc.count_by(spacy.attrs.POS)
print(count)

for k,v in count.items():
    print(doc.vocab[k].text,"|",v)
    
nouns=[]
for token in doc:
    if token.pos_=="NOUN":
        nouns.append(token)

print(nouns)
    



# for k,v in count.items():
#     print(doc.vocab[96].text,"|",v)
