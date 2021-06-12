import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

data = {}
data['root'] = []
endPage = 700
for page in range (1,endPage+1):
    url = 'https://www.thepoke.co.uk/page/' + str(page) + '/' 
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html5lib')
    article = soup.find_all('article', class_= 'boxgrid')
    for link in article:
        mylink = BeautifulSoup(str(link), 'html.parser')
        gettinglink = mylink.find('a', href=True)
        try:
            getArticle = link.p.string
        except:
            continue
        data['root'].append({
            'is_sarcastic': 1,
            'headline': str(getArticle),
            'article_link': str(gettinglink['href'])})
with open('thepoke.json', 'w') as f:
    json.dump(data, f, indent = 3)
print(len(data['root']))