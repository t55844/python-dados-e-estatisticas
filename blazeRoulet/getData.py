from selenium import webdriver
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
"""
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