from bs4 import BeautifulSoup
import requests

website = requests.get("https://news.ycombinator.com/news")
yc_web_page = website.text
print(yc_web_page)

soup = BeautifulSoup(website.content, "html.parser")
article = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in article :
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find(name="span", class_="score")]
# print(article_texts)
# print(article_links)
# print(article_upvote)

largest_numbers = max(article_upvote)
largest_index = article_upvote.index(largest_numbers)

print(article_texts[largest_index])


# with open("website.html", encoding='utf-8') as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
# # print(soup.p)

# all_anchor_tags = soup.find_all(name="a")
# # for anchor in all_anchor_tags:
# #     print(anchor.getText())

# heading = soup.find(name="h1", id="name")
# # print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# h3_heading = soup.find_all(name="h3", class_="heading")
# print(h3_heading)

# name = soup.select_one(selector="#name")
# print(name)

# heading = soup.select(selector=".heading")
# print(heading)

