# NOT TO BE USED IN MAIN CODE
from keywords_list import positive_keywords
from collections import Counter 
from nltk.corpus import stopwords
import nltk, re

with open(r'Day 93 - Webscraping job requirements\.misc\job_descriptions.txt', 'r', encoding="utf-8") as f:
    job_desctiptions = f.read()


def initial_word_analysis(analyzed_descriptions):
    # FILTERING OUT SPECIAL CHARACTERS
    words_list = analyzed_descriptions.split()
    pattern = r'[^a-zA-Z\s]'
    no_special_char_list = []
    for word in words_list:
        word = re.sub(pattern, '', word)
        if len(word) > 1:
            no_special_char_list.append(word)

    # FILTERING OUT COMMON WORDS
    nltk.download('punkt')
    nltk.download('stopwords')
    no_eng_stopwords_list = [word.lower() for word in no_special_char_list if word not in stopwords.words('english')]

    # COUNTING MOST COMMON WORDS
    keyword_counts = Counter(no_eng_stopwords_list)
    most_common_words = keyword_counts.most_common(500)

    return most_common_words


def bulletpoint_analysis(analyzed_descriptions):
    bulletpoint_list = analyzed_descriptions.split('\n')
    job_requirements_list= []
    differencies_list = []
    experience_list = []
    for bulletpoint in bulletpoint_list:
        if 'experience' in bulletpoint:  # and 'year' in bulletpoint:
            experience_list.append(bulletpoint)
        if any(keyword in bulletpoint for keyword in positive_keywords):
            job_requirements_list.append(bulletpoint)
        else:
            differencies_list.append(bulletpoint)

    return job_requirements_list, experience_list, differencies_list

