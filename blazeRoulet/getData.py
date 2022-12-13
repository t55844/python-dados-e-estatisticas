"""from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

from login import Login

from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter

service = Service(GeckoDriverManager().install())

options = Options()
#options.add_argument('--headless')
options.add_argument('window-size=400,800')

driver = webdriver.Firefox(service=service, options=options)

driver.get('https://blaze.com/pt')

test1: Login = Login( driver)
test1.login()



navegador.get('https://blaze.com/pt/games/double')
sleep(2)
soup = BeautifulSoup(navegador.page_source, 'html.parser')

div_container_number = soup.find_all(attrs={"class": "roulette-previous casino-recent"})
div_with_number = div_container_number[0].findNext().findAll(attrs={'class': 'roulette-tile'})

with open('blazeDoubleRoulet.csv','w') as arquivo:
    cabecalho = ['Cor', 'Numero']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    for div in div_with_number:
        cor = div.findNext().attrs['class'][1]
        numero = div.getText()
        escritor_csv.writerow({'Cor': cor, 'Numero': numero})

"""


import requests

cookies = {
    '_ga': 'GA1.2.939124625.1669586405',
    '__zlcmid': '1D9lPOpVlbC2We2',
    '_gid': 'GA1.2.1731432165.1670774803',
    '_gat': '1',
}

headers = {
    'authority': 'blaze.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://blaze.com/pt/games/double',
    'sec-ch-ua': '^\^Opera',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\^Windows^^',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0',
    'x-client-language': 'pt',
    'x-client-version': '32c436ce5',
}

response = requests.get('https://blaze.com/api/roulette_games/recent', headers=headers, cookies=cookies)
print(response.content)