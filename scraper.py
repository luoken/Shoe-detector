import requests
from bs4 import BeautifulSoup

adidasUrl = "https://www.zappos.com/adidas-men-shoes/CK_XAVoBAcABAuICAwELGA.zso"
nikeUrl = "https://www.zappos.com/nike-men-shoes/CK_XAVoBb8ABAuICAwELGA.zso"
vansUrl =   "https://www.zappos.com/vans-men-shoes/CK_XAVoCqwHAAQLiAgMBCxg.zso"


def scrape(url):
  page = requests.get(url)
  soup = BeautifulSoup(page, 'lxml')

  print(soup);

scrape(adidasUrl)
