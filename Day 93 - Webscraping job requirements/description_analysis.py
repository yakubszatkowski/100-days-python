from collections import Counter 
import numpy as np
import re

with open(r'Day 93 - Webscraping job requirements\.misc\job_descriptions.txt', 'r', encoding="utf-8") as f:
    job_desctiptions = f.read()

words_list = job_desctiptions.split()

clean_word_list = []
pattern = r'[^a-zA-Z\s]'
for word in words_list:
    word = re.sub(pattern, '', word)
    if len(word) > 1:
        clean_word_list.append(word)

words_array = np.array(clean_word_list)
unique_words, count = np.unique(words_array, axis=0, return_counts=True)
top_10_indices = np.argsort(count)[-200:][::-1]
list_top_words = []
for index in top_10_indices:
    common_word = unique_words[index].tolist()
    list_top_words.append(common_word)

for word in list_top_words:
    print(word)
