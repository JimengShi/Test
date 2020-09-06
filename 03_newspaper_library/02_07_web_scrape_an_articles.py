# PS:
# (1) install libraries: nltk, newspaper, newspaper3k
# (2) please make sure import nltk to download "punkt" at first, then it's good to import newspaper


# import nltk
# nltk.download('punkt')
import newspaper
import pandas as pd
from newspaper import Article

#The Basics of downloading the article to memory
article = Article("https://www.gamespot.com/articles/epics-fortnite-ban-and-apple-google-legal-battle-e/1100-6480913/")
article.download()
article.parse()
article.nlp()

temp_df = pd.DataFrame(columns = ['Title', 'Authors', 'Text', 'Keywords',
                                'Summary', 'published_date', 'Source'])

temp_df['Authors'] = article.authors
temp_df['Title'] = article.title
temp_df['Text'] = article.text
temp_df['Summary'] = article.summary
temp_df.at[0, 'Keywords'] = article.keywords
temp_df['published_date'] = article.publish_date
temp_df['Source'] = article.source_url
temp_df


# print('Title:\n', article.title)        # Gives the title
# print('---------------')
# print('Summary:\n', article.summary)    # To print out a summary of the text. This works, because newspaper3k has built in NLP tools
# print('---------------')
# print('Text:\n', article.text)          # To print out the full text
# print('---------------')
# print('Authors:\n', article.authors)    # To print out the list of authors
# # print('---------------')
# print('Keywords:\n', article.keywords)  # To print out the list of keywords
# print('---------------')
# print('Publish date:\n', article.publish_date)   # Gives the date the article was published
# print('---------------')
# print('Top Image:\n', article.top_image)         # Gives the link to the main image of the article
# print('---------------')
# print('Images:\n', article.images)               # Provides a set of image links

temp_df.to_csv('my_scraped_an_article.csv')