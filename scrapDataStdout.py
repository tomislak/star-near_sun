#!/home3/etokral/gitovi/scraping/bin/python3

import requests
from bs4 import BeautifulSoup

url = 'http://phl.upr.edu/projects/nearby-stars-catalog'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
#print(soup.prettify())
starsList = soup.find('font', face="'courier new', monospace").find_all('b')

for oneStar in starsList:
    lajn = oneStar.get_text()
    # ID Name           Proper Name         Type       D(ly)     M(SU)     R(SU)   Teff(K)   Planets
    _id = lajn[:4]
    _name = lajn[6:21]
    _properName = lajn[21:41]
    _type = lajn[41:52]
    _Dly = lajn[52:62]
    _MSU = lajn[62:72]
    _RSU = lajn[72:80]
    _teffK = lajn[80:90]
    _planets = lajn[90:97]
    print(f'{_id} # {_name} # {_properName} # {_type} # {_Dly} # {_MSU} # {_RSU} # {_teffK} # {_planets} #')
