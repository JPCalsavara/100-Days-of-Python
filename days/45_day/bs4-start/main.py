from bs4 import BeautifulSoup  # Corrigida a importação
import lxml
import requests

# # Abrir o arquivo HTML
# with open("website.html", "r", encoding="utf-8") as file:
#     contents = file.read()
#
# # Criar o objeto BeautifulSoup
# soup = BeautifulSoup(contents, "html.parser")
#
# # # Imprimir o título da página
# # print(soup.prettify())
# #
# # all_anchor_tags = soup.find_all(name="a")
# #
# # for tag in all_anchor_tags:
# #     print(tag.getText())
# #
# # heading = soup.find(name="h1",id="name")
# # print(heading)
# #
# # section_heading = soup.find(name="h3",class_="heading")
#
# company_url = soup.select_one(selector="p a")
# heading = soup.select_one(selector=".heading")
# #select the tag like a css file

response = requests.get(url="https://appbrewery.github.io/news.ycombinator.com/")
#get the web site html data

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage,"html.parser")

articles = soup.find_all(name="a",class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]
# max_score = 0
# max_index = 0
# for score in article_upvote:
#     if score > max_score:
#         max_index = article_upvote.index(score)
#         max_score = score
# print(max_score)
# print(articles[max_index])
largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
