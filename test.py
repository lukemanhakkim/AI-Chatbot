import requests
import json

url = ('https://newsapi.org/v2/everything?'
       'q=Tamilnadu&'
       'from=2019-11-04&'
       'sortBy=popularity&'
       'apiKey=c01f99cf572845e7953fc944bb674659')

response = requests.get(url)
r=response.json()
news_list = r['articles']
for news in news_list:
       title = news['title']
       description = news['description']
       url = news['url']
       #print("n")'''
       print("""{0},
			    {1},
			    {2}""".format(title, description, url))
"""
from GoogleNews import GoogleNews
googlenews = GoogleNews()

googlenews.search('Carleton University')
#print(googlenews.getlinks())
#print(googlenews.gettext())
print(googlenews.result())
news_dict = googlenews.result()
for news in news_dict:
       print(news['title'])"""


"""from google import search
import urllib
from bs4 import BeautifulSoup

def google_scrape(url):
    thepage = urllib.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text

i = 1
query = 'search this'
for url in search(query, stop=10):
    a = google_scrape(url)
    print(str(i) + ". " + a)
    print(url)
    print(" ")
    i += 1"""