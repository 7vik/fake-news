#!/usr/bin/env python

import os
import re
# import langdetect
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from general_funcs import *
stopwords_set = set(stopwords.words("english"))

original_message= 'All of those people who registered to vote because she made some emotional plea on behalf of fake victims and "democracy" should be ashamed of themselves'
tokens = []
decontracted_message = decontracted(original_message).capitalize() ## decontract and capitalize
temp = word_tokenize(original_message)
for i in temp:
    for k in camel_case_split(i):
        tokens.append(k)
tagged_sentence = pos_tag(tokens)
print("Tagged sentence: ")
print(tagged_sentence)

print("After stopword removal: ")
tagged_sentence_without_stopwords_set = [(word, tag) for word, tag in tagged_sentence if(word not in stopwords_set)]
print(tagged_sentence_without_stopwords_set)
