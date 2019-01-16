#!/usr/bin/env python

import numpy as np
import pandas as pd
import general_funcs
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import tree


BASE_URL_1 = "../teamName/training/celebrityDataset/"
BASE_URL_2 = "../teamName/training/fakeNewsDataset/"
print("loading data...")

f = open('glove.6B.100d.txt')
embeddings_index = dict()
for line in f:
	values = line.split()
	word = values[0]
	coefs = np.asarray(values[1:], dtype='float32')
	embeddings_index[word] = coefs
f.close()

def load_fromdir(BASE_URL):
    file_list = os.listdir(BASE_URL)
    res_list = []
    for fileid in file_list:
        opened = open(BASE_URL+fileid)
        text = opened.read()
        res_list.append(text)
    print(len(res_list))
    return res_list

fake_list = load_fromdir(BASE_URL_1+"fake/")
real_list = load_fromdir(BASE_URL_1+"legit/")
fake_list.extend(load_fromdir(BASE_URL_2+"fake/"))
real_list.extend(load_fromdir(BASE_URL_2+"legit/"))
print("loaded!")
total = real_list+fake_list
targets = [1 for i in real_list]+[0 for i in fake_list]
total_as_vectors = []
tfidf = TfidfVectorizer ()
tfidf.fit(total)
tfidf_dict = dict(zip(tfidf.get_feature_names(), tfidf.idf_))
import nltk

for i in total:
    my_vector = np.ndarray((100))
    tokenized = nltk.word_tokenize(general_funcs.remove_punctuations(" ".join(general_funcs.camel_case_split(i))))
    for j in tokenized:
        try:
            my_vector +=embeddings_index[j.lower()]
        except:
            print("Missed a word")
            print(j)
            continue
    total_as_vectors.append(my_vector)

from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values=np.nan, strategy="mean")
imp.fit(total_as_vectors)
total_as_vectors= imp.transform(total_as_vectors)
X_train, X_test, y_train, y_test = train_test_split(total_as_vectors, targets, random_state=0)
from sklearn import svm
clf = svm.SVC()
clf.fit(X_train,y_train)
print(clf.score(X_test, y_test))

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

print("Train accuracy {}".format(logreg.score(X_train,y_train)))
print("Test accuracy {}".format(logreg.score(X_test,y_test)))

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
