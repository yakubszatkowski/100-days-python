from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
yc_web = response.text

soup = BeautifulSoup(yc_web, 'html.parser')

articles = soup.find_all(name='span', class_='titleline')
articles_upvotes = soup.find_all(name='span', class_='score')

article_texts = []
article_links = []
for article in articles:
    text = article.find(name='a').getText()
    link = article.get('href')
    article_texts.append(text)
    article_links.append(link)

article_upvotes = [int(upvote_count.getText().split(' ')[0]) for upvote_count in articles_upvotes]

# highest_score = 0
# for score in article_upvotes:
#     if score > highest_score:
#         highest_score = score

# or
highest_score = max(article_upvotes)

index = article_upvotes.index(highest_score)
print(f'{article_texts[index]} - {article_links[index]}')

