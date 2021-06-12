import requests
from bs4 import BeautifulSoup
import json
data = {}
data['root'] = []
NUMBER_OF_PAGES = 100
for i in range(1, NUMBER_OF_PAGES + 1):
    url = "http://www.thecivilian.co.nz/page" + str(i) + "/"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html5lib')
    h2 = soup.find_all('h2')    
    for link in h2:
        try:
            mylink = BeautifulSoup(str(link), 'html.parser')
            gettinglink = mylink.find('a', href=True)
            data['root'].append({
                'is_sarcastic': 0,
                'headline': str(gettinglink.find(text=True)),
                'article_link': str(gettinglink['href'])})
        except:
            pass
        
with open('thecivilian.json', 'w') as f:
    json.dump(data, f, indent=3)
print('Done')