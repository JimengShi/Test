import nltk
nltk.download('punkt')
import newspaper
import pandas as pd
from newspaper import Article
import lxml
import requests
from bs4 import BeautifulSoup

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
url = 'https://www.bbc.com/news/'
page_text = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(page_text, features=lxml)

list_url = soup.select('.gs-c-promo-body gel-1/2@xs gel-1/1@m gs-u-mt@m a')
for li in list_url:
    article_url = 'https://www.bbc.com/' + li.a['href']
    print(article_url)
# cnn_paper = newspaper.build('https://cnn.com/')
#
# for i, category in enumerate(cnn_paper.category_urls()):
#     print(i, category)
#
#     #The Basics of downloading the article to memory
#     article = Article("https://www.gamespot.com/articles/epics-fortnite-ban-and-apple-google-legal-battle-e/1100-6480913/")
#     article.download()
#     article.parse()
#     article.nlp()
#
#     temp_df = pd.DataFrame(columns = ['Title', 'Authors', 'Text', 'Keywords',
#                                     'Summary', 'published_date', 'Source'])
#
#     temp_df['Authors'] = article.authors
#     temp_df['Title'] = article.title
#     temp_df['Text'] = article.text
#     temp_df['Summary'] = article.summary
#     temp_df.at[0, 'Keywords'] = article.keywords
#     temp_df['published_date'] = article.publish_date
#     temp_df['Source'] = article.source_url
#     temp_df
#
#
#     # print('Title:\n', article.title)        # Gives the title
#     # print('---------------')
#     # print('Summary:\n', article.summary)    # To print out a summary of the text. This works, because newspaper3k has built in NLP tools
#     # print('---------------')
#     # print('Text:\n', article.text)          # To print out the full text
#     # print('---------------')
#     # print('Authors:\n', article.authors)    # To print out the list of authors
#     # # print('---------------')
#     # print('Keywords:\n', article.keywords)  # To print out the list of keywords
#     # print('---------------')
#     # print('Publish date:\n', article.publish_date)   # Gives the date the article was published
#     # print('---------------')
#     # print('Top Image:\n', article.top_image)         # Gives the link to the main image of the article
#     # print('---------------')
#     # print('Images:\n', article.images)               # Provides a set of image links
#
# temp_df.to_csv('my_scraped_an_article.csv')