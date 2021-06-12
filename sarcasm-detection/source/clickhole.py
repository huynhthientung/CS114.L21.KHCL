import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

data = {}
data['root'] = []
endPage = 360
for page in range (1,endPage+1):
    url = 'https://clickhole.com/page/' + str(page) + '/' 
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html5lib')
    h2 = soup.find_all('h2', class_= 'post-title')
    for link in h2:
        mylink = BeautifulSoup(str(link), 'html.parser')
        gettinglink = mylink.find('a', href=True)
        try:
            getArticle = mylink.find('a', text=True).string
        except:
            continue
        data['root'].append({
            'is_sarcastic': 1,
            'headline': str(getArticle),
            'article_link': str(gettinglink['href'])})
with open('clickhole.json', 'w') as f:
    json.dump(data, f, indent = 3)
print(len(data['root']))