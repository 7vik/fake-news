#!/usr/bin/env python
import general_funcs
import nltk
import numpy as np
import general_funcs
from sklearn import tree
from collections import Counter

stopwords_set = set(nltk.corpus.stopwords.words("english"))
corpus_root = "./corpus" ## This might not work on windows.
wordlists = nltk.corpus.PlaintextCorpusReader(corpus_root,".*")
lovecraft = wordlists.words("hplovecraft.txt")
isaac = wordlists.words("isaacasimov.txt")
isaac_pairs = [("isaac", word) for word in isaac]
lovecraft_pairs = [("lovecraft", word) for word in lovecraft]
dataset = isaac_pairs + lovecraft_pairs
cfd = nltk.ConditionalFreqDist((author, word) for author, word in dataset)
term_list = ["CC","CD","DT","EX","FW","IN","JJ","JJR",'JJS','LS','MD',"NN",'NNS','NNP','NNPS','PDT','POS','PRP','PRP$','RB','SYM','TO','UH','VB','VBD','VBG','VBN','VBP','VBZ','WDT','WP','WP$','WRB']
training_data=[]
results = []
def get_sent_attr(sent,length = None):
    tagged = nltk.pos_tag(sent)
    counts = Counter(tag for word, tag in tagged)
    if(length is None):
        length = len(sent)
    sample=[length]
    for i in range(len(term_list)):
        sample.append(counts[term_list[i]])
    freq_dist = nltk.FreqDist(w.lower() for w in isaac)
    sample +=[freq_dist[k] for k in ['a',',','in','of',]]
    return sample

for fileid in wordlists.fileids():
    avg = sum(len(sent) for sent in wordlists.sents(fileids=[fileid])) / len(wordlists.sents(fileids=[fileid]))
    print(fileid, avg)
    print("Most common words Isaac")
    print(nltk.FreqDist(w.lower() for w in isaac)[","])
    print("Without stopwords")
    print(nltk.FreqDist(w.lower() for w in isaac if w not in stopwords_set).most_common(10))
    print("Most common words Lovecraft")
    print(nltk.FreqDist(w.lower() for w in lovecraft).most_common(10))
    print("Without stopwords")
    print(nltk.FreqDist(w.lower() for w in lovecraft if w not in stopwords_set).most_common(10))

for i, sent in enumerate(wordlists.sents(fileids="hplovecraft.txt")):
    training_data.append(get_sent_attr(sent))
    results.append(-1)

for i, sent in enumerate(wordlists.sents(fileids="isaacasimov.txt")):
    training_data.append(get_sent_attr(sent))
    results.append(1)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(training_data, results)
test_str = "On the occasion of the visit, ran the professor’s manuscript, the sculptor abruptly asked for the benefit of his host’s archaeological knowledge in identifying the hieroglyphics on the bas-relief. He spoke in a dreamy, stilted manner which suggested pose and alienated sympathy; and my uncle shewed some sharpness in replying, for the conspicuous freshness of the tablet implied kinship with anything but archaeology. Young Wilcox’s rejoinder, which impressed my uncle enough to make him recall and record it verbatim, was of a fantastically poetic cast which must have typified his whole conversation, and which I have since found highly characteristic of him."
test_len = len(test_str.split())/len(test_str.split("."))
print("and for the test file the avg sent lenght is :")
print(test_len)
test_attr= [get_sent_attr(w) for w in test_str.split(".")]
print("And the test results are...")
prediction = 0
for pred in clf.predict(test_attr):
    prediction += pred
prediction = prediction/len(test_attr)
ans = "HP Lovecraft" if (prediction < 0 ) else "Isaac Asimov"
print(ans)
