#!/home3/etokral/gitovi/scraping/bin/python3

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_nearest_stars_and_brown_dwarfs'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
#print(soup.prettify())
starsList = soup.find('table', class_='sortable').find_all("tr")

for oneStar in starsList:
    p1 = []
    for oneData in oneStar.find_all('td'):
        #print(oneData.get_text())
        p1.append(oneData.get_text().rstrip())
    for i in p1:
        print(i, end='=')
    #print(p1)
    print("---")
