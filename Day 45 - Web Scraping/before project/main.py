from bs4 import BeautifulSoup

with open ('website.html') as file:
    contents = file.read()
soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.prettify())
# print(soup.find_all(name="li"))

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get('href'))
#
# heading = soup.find(name='h1', id='name')
# print(heading)

subheading = soup.find(name='h3', class_='heading')
print(subheading)
# print(subheading.name)
# print(subheading.getText())
# print(subheading.get('class'))

# # selecting element with p and a tags
# company_url = soup.select_one(selector='p a')
# print(company_url)

# # selecting element with specified id
# name = soup.select_one(selector='#name')
# print(name)

# # selecting element of heading class, no need for "selector="
# classes = soup.select('.heading')
# print(classes)
