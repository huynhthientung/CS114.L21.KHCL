import requests
from bs4 import BeautifulSoup
import json
data = {}
data['root'] = []
NUMBER_OF_PAGES = 1 # May, 2018 to present
for i in range(1, NUMBER_OF_PAGES + 1):
    url = "https://www.thebeaverton.com/page/" + str(i) + "/"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html5lib')
    h2 = soup.find_all('h3', {'itemprop': 'headline'}, )
    for link in h2:
        mylink = BeautifulSoup(str(link), 'html.parser')
        gettinglink = mylink.find('a', href=True)
        # writer.writerow({'Headline': str(gettinglink.find(text=True)), 'Link': str(gettinglink['href'])})
        data['root'].append({
            'is_sarcastic': 1,
            'headline': str(gettinglink.find(text=True)),
            'article_link': str(gettinglink['href'])})
with open('thebeaverton.json', 'w') as f:
    json.dump(data, f, indent=3)
print('Done')