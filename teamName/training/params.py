import os
from pprint import pprint as p
global article 
import matplotlib
from nltk import FreqDist
from nltk import word_tokenize
import nltk
import csv


article = 0

params = []
for i in range(1,251):
    f = open("./celebrityDataset/fake/"+str(i).zfill(3)+"fake.txt", "r+")
    fdict = {}
    fdict["Index"] = article
    article += 1
    fdict["Verdict"] = 0
    fdict["Title"] = f.readline()
    fdict["Text"] = ''.join(f.read().split('\n'))
    fdict["Title Length"] = len(fdict["Title"]) / 250
    freq_dist = FreqDist(fdict["Text"].split(' '))
    fdict["Word Count"] = len(fdict["Text"].split(' '))

    common_words = []
    t = 0
    y = 0
    for w in set(fdict["Text"].split(' ')):
        if len(w) > 3 and freq_dist[w] > 0.01*fdict["Word Count"] and t<5:
            common_words.append((w, freq_dist[w]))
            y += freq_dist[w]
            t += 1

    fdict["Common Words"] = common_words
    fdict["Sum of Common"] = y

    fdict["SimpleAdj"] = 0
    fdict["SuperComparatives"] = 0
    temp = nltk.pos_tag(word_tokenize(fdict["Text"]))
    for r, tag in temp:
        if tag == "JJ" or tag == "RB":
            fdict["SimpleAdj"] += 1
            #print(fdict["Adjectives"])
        elif tag == "JJR" or tag == "RBR" or tag == "RBS" or tag == "JJS":
            fdict["SuperComparatives"] += 1

    fdict["SimpleAdj"] /= fdict["Word Count"]
    fdict["SuperComparatives"] /= fdict["Word Count"]

    params.append(fdict)


 #   fdict["Avg Word Size"] = 



for i in range(1,251):
    f = open("./celebrityDataset/legit/"+str(i).zfill(3)+"legit.txt", "r+")
    fdict = {}
    fdict["Index"] = article
    article += 1
    fdict["Verdict"] = 1
    fdict["Title"] = f.readline()
    fdict["Text"] = ''.join(f.read().split('\n'))
    fdict["Title Length"] = len(fdict["Title"]) / 250
    fdict["Word Count"] = len(fdict["Text"].split(' '))
    freq_dist = FreqDist(fdict["Text"].split(' '))
    common_words = []
    t = 0
    y = 0
    for w in set(fdict["Text"].split(' ')):
        if len(w) > 3 and freq_dist[w] > 0.01*fdict["Word Count"] and t<5:
            common_words.append((w, freq_dist[w]))
            y += freq_dist[w]
            t += 1

    fdict["Common Words"] = common_words
    fdict["Sum of Common"] = y

    fdict["SimpleAdj"] = 0
    fdict["SuperComparatives"] = 0
    temp = nltk.pos_tag(word_tokenize(fdict["Text"]))
    for r, tag in temp:
    #    print(r)
    #    print(tag)
        if tag == "JJ" or tag == "RB":
            fdict["SimpleAdj"] += 1
            #print(fdict["Adjectives"])
        elif tag == "JJR" or tag == "RBR" or tag == "RBS" or tag == "JJS":
            fdict["SuperComparatives"] += 1

    fdict["SimpleAdj"] /= fdict["Word Count"]
    fdict["SuperComparatives"] /= fdict["Word Count"]
    params.append(fdict)
    


#p(params)

fake_title_length = 0
legit_title_length = 0

fake_sum_of_common_word_freqs = 0
legit_sum_of_common_word_freqs = 0

fake_SimpleAdj = 0
fake_SuperComparatives = 0
legit_SimpleAdj = 0
legit_SuperComparatives = 0

for art in params:
    if art["Verdict"]==0:   #fake
        fake_SimpleAdj += art["SimpleAdj"]
        fake_SuperComparatives += art["SuperComparatives"]
        for word, counts in art["Common Words"]:
            fake_sum_of_common_word_freqs += counts
        fake_title_length += art["Title Length"]
    else:  #legit
        legit_SimpleAdj += art["SimpleAdj"]
        legit_SuperComparatives += art["SuperComparatives"]
        for word, counts in art["Common Words"]:
            legit_sum_of_common_word_freqs += counts
        legit_title_length += art["Title Length"]

#print(fake_sum_of_common_word_freqs)
#print(legit_sum_of_common_word_freqs)

#print(100 * fake_supri)
#print(100 * legit_supri)


#param is a list of dictionaries - Index, Verdict, Word Count, Title Length, Common Words, SimpleAdj, SuperComparatives

with open("parameters_extracted.csv", "w+") as f:
    out_write = csv.writer(f)
    for art in params:
        out_write.writerow([art["Index"],art["Verdict"], art["Word Count"], art["Title Length"], art["Sum of Common"], art["SimpleAdj"], art["SuperComparatives"]])