from keywords_list import positive_keywords
from collections import Counter 
import re

with open(r'Day 93 - Webscraping job requirements\.misc\job_descriptions.txt', 'r', encoding="utf-8") as f:
    job_desctiptions = f.read()


def keyword_count(analyzed_descriptions):
    words_list = analyzed_descriptions.split()
    no_special_char_list = []

    # CLEANING SPECIAL CHARACTERS, NON-ENGLISH CHARACTERS, SINGLE LETTER WORDS
    pattern = r'[^a-zA-Z\s]'
    for word in words_list:
        word = re.sub(pattern, '', word)
        if len(word) > 1:
            no_special_char_list.append(word)

    # FILTERING TECH WORDS
    tech_words_list = [word for word in no_special_char_list if word in positive_keywords]

    # COUNTING WORDS
    keyword_counts = Counter(tech_words_list)
    most_common_words = keyword_counts.most_common(100)

    return most_common_words

words = keyword_count(job_desctiptions)

for x in words:
    print(x)
