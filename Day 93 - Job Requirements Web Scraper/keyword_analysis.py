from keywords_list import positive_keywords
from collections import Counter 
import re


def keyword_count(analyzed_descriptions):
    # Creating list of words of whole descriptions' texts
    words_list = analyzed_descriptions.split()
    no_special_char_list = []

    # Cleaning special characters, non-english characters, single letter words
    pattern = r'[^a-zA-Z\s]'
    for word in words_list:
        word = re.sub(pattern, '', word)
        if len(word) > 1:
            no_special_char_list.append(word)

    # Filtering technology related words
    tech_words_list = [word for word in no_special_char_list if word in positive_keywords]

    # Counting
    keyword_counts = Counter(tech_words_list)
    most_common_words = keyword_counts.most_common(150)

    return most_common_words

