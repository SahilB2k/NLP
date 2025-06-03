import nltk 
import spacy

from nltk.stem import PorterStemmer

stemmer=PorterStemmer()

words=["eating","drawing","manageable","drinking","sleeping"]

for word in words:
    print(word,"|",stemmer.stem(word) ) 
    
#stemming just removes the suffix and is not smart enough then lemmitization
#but is faster