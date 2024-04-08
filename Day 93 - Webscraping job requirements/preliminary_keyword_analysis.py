# NOT TO BE USED IN MAIN CODE

from collections import Counter 
from nltk.corpus import stopwords
import nltk, re

with open(r'Day 93 - Webscraping job requirements\.misc\job_descriptions.txt', 'r', encoding="utf-8") as f:
    job_desctiptions = f.read()

# FILTERING OUT SPECIAL CHARACTERS
words_list = job_desctiptions.split()
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

# PRINTING
for technology in most_common_words:
    print(technology)

#TODO
# find most revelant technology related keywords
