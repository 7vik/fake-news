import nltk
import pandas as pd
import os
import general_funcs

def clean_content(text):
    list_apos = text.split('â')
    apos = len(list_apos)
    text = "'".join(list_apos)
    text = ''.join(text.split('Â'))
    print("Cleaned of "+str(apos)+" Special Characters")
    text = text.split('© 2019 Reuters. All Rights Reserved.')[0]
    text = text.split('© 2018 Reuters. All Rights Reserved.')[0]
    text = text.split('Your email address will not be published.')[0]
    while text[0]==' ':
        text = text[1:]
    if text[0]=='2':
        return text[4:]
    else:
        return text




path_to_data = os.path.abspath("./../datasets/final_dataset.csv")
data = pd.read_csv(path_to_data, encoding="ISO-8859-1")
data = data.dropna(axis="columns",how="all")
data = data.dropna(axis="rows", subset=["Title","Text"])
data = data.dropna(axis="columns")

data["Text"] = data.apply(lambda row: clean_content(row["Text"]), axis=1)
'''
data["tok_cont"] = data.apply(lambda row: nltk.word_tokenize(row["Text"]),axis=1)
data["tok_title"] = data.apply(lambda row: nltk.word_tokenize(row["Title"]),axis=1)
data["pos_cont"] = data.apply(lambda row: nltk.pos_tag(row["tok_cont"]),axis=1)
data["pos_title"] = data.apply(lambda row: nltk.pos_tag(row["tok_title"]),axis=1)
data["wc_cont"] = data.apply(lambda row: set(row["tok_cont"]),axis=1)
data["wc_title"] = data.apply(lambda row: set(row["tok_title"]),axis=1)
'''
print(clean_content(data.iloc[4032][1]))

#print(data[1])
