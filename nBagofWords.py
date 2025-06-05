# it is a extension to bag of words where we pair two or multiple words together to see their occurence and compare various documents
# the n decides the number of words which will be paired
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from spacy.lang.en.stop_words import stopword

nlp=spacy.load("en_core_web_sm")


v=CountVectorizer(ngram_range=(1,1)) # creates vocabulary of single words only
# v=CountVectorizer(ngram_range=(1,2)) # creates vocab of single and paired words
# v=CountVectorizer(ngram_range=(1,2)) # creates vocab of paired words only
text=nlp("Thor Hathodewala is looking for job")
text_refined=[] # storing lemmatized words only
for token in text:
    if token.lemma_:
        if not token.is_stop:
            
            text_refined.append(token.lemma_)

print("lemmatized text:",text_refined)
# refined_text=" ".join([token.text for token in text_refined])
refined_text=" ".join(text_refined) # converting the list to string since countVectorizer takes only string as an input
print("Input string:",refined_text)

    
v.fit([refined_text])

print("vocabs:",v.vocabulary_)
print(v.transform([refined_text]).toarray())