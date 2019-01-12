#!/usr/bin/env python

import os
import re
# import langdetect
import general_funcs
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stopwords_set = set(stopwords.words("english"))
my_sentence = "Are you set for the party?"
my_sentence_tokenized = [(word,general_funcs.osa_distance(word,"party",ignore_case=True)) for word in word_tokenize(my_sentence) if word not in stopwords_set]
my_sentence_tokenized.sort(key=lambda x: x[1])
print(my_sentence_tokenized)
threshold = 0 ## Set higher values to allow more inaccurate results eg "praty"
if my_sentence_tokenized[0][1] > threshold:
    print("Not party")
else:
    print("Party")
