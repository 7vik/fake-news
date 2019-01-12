import general_funcs
import nltk

sentence= "pretty little lady"
take = general_funcs.decontracted(sentence)
take = general_funcs.remove_punctuations(take)
take = nltk.word_tokenize(take)
bigrams = [take[i]+' '+take[i+1] for i in range(len(take)-1)]
for bigram in bigrams:
    print(bigram)

print('Total No. of Bigrams:', len(bigrams))
tagged = nltk.pos_tag(take)

hyphenating_rule = r'''
hyphenate: {<VB.?>+<IN>}
alt_hyphen: {<RB|JJ>+<NN|NNS>+}
'''
chunkParser = nltk.RegexpParser(hyphenating_rule)
chunked = chunkParser.parse(tagged)
print("Compound words:")
hyphenated = []
for subtree in chunked.subtrees(filter=lambda t:t.label()!="S"):
    hyphenated.append("-".join([a for (a, b) in subtree.leaves()]))
print(hyphenated)
