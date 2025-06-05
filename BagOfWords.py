# Bag of Words is used for text represeantation
# text represetation describes the text as a set of numbers
# disadv - the vocablury can be of great size , hence requires more computational energy

import pandas as pd
import numpy as np

df=pd.read_csv("spam_ham_dataset.csv")
# print(df.info())
# print(df.label.value_counts())

df['spam']=df["label"].apply(lambda x : 1 if x=="spam" else 0)
# print(df.head())

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(df.text,df.spam, test_size=0.2)
# print(X_train.shape)
# print(X_train[:4])

from sklearn.feature_extraction.text import CountVectorizer
v=CountVectorizer()

X_train_cv=v.fit_transform(X_train.values)
# print(X_train_cv)
print(X_train_cv.shape)
print(X_train_cv.toarray()[:2][0])
print(v.get_feature_names_out()[11207])
# print(v.vocabulary_)
# print(v.vocabulary_)

