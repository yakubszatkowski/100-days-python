from collections import Counter 

with open(r'.misc\job_descriptions.txt', 'r', encoding="utf-8") as f:
    job_desctiptions = f.read()

words_list = job_desctiptions.split()
counter = Counter(words_list)
most_common_words = counter.most_common(400)

for word in most_common_words:
    print(word)
