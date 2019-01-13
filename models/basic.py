#!/usr/bin/env python

import nltk
import pandas as pd
import os
import general_funcs

path_to_data = os.path.abspath("./../datasets/wndr_dataset.csv")
data = pd.read_csv(path_to_data)
data = data.dropna(axis=0)
data["tok_cont"] = data.apply(lambda row: nltk.word_tokenize(row["Content"]),axis=1)
data["tok_title"] = data.apply(lambda row: nltk.word_tokenize(row["Title"]),axis=1)
data["pos_cont"] = data.apply(lambda row: nltk.pos_tag(row["tok_cont"]),axis=1)
data["pos_title"] = data.apply(lambda row: nltk.pos_tag(row["tok_title"]),axis=1)
data["wc_cont"] = data.apply(lambda row: set(row["tok_cont"]),axis=1)
data["wc_title"] = data.apply(lambda row: set(row["tok_title"]),axis=1)
