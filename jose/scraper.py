import requests
import lxml
import urllib
from bs4 import BeautifulSoup

# https://www.zappos.com/vans-men-shoes/CK_XAVoCqwHAAQLiAgMBCxg.zso?p=0


adidas = "https://www.zappos.com/adidas-men-shoes/CK_XAVoBAcABAuICAwELGA.zso"
nike = "https://www.zappos.com/nike-men-shoes/CK_XAVoBb8ABAuICAwELGA.zso"
vans =   "https://www.zappos.com/vans-men-shoes/CK_XAVoCqwHAAQLiAgMBCxg.zso"

def saveImg(url, brand, n):
  name = brand + '-'  +  str(n) + '.jpg'
  urllib.urlretrieve(url, name)


def scrape(url):
  r = requests.get(url)
  productLinks = []
  pageList = []

  if(r.status_code == 200):
    soup = BeautifulSoup(r.content, "lxml")
    productLinks = soup.find_all("a", class_='product')

    for i in productLinks:
      pageList.append(i.get('href'))

    for i in range(50):
      if 'adidas' in url:
        brandName = 'adidas'
      elif 'nike' in url:
        brandName = 'nike'
      else:
        brandName = 'vans'

    for i in pageList:
      # scrape productPage with url
      # print("https://www.zappos.com" + i)
      print('-------------------------------------------------------------------------')
      scrapeProductPage("https://www.zappos.com" + i)
      print('-------------------------------------------------------------------------')

    print(len(pageList))

  else:
    print("Error: Response Status Code != 200")
    print("Error: Ask Jose why it broke.")


def scrapeProductPage(url):
  print(url)
  r = requests.get(url)
  # only want 3, 5
  if(r.status_code == 200):
    soup = BeautifulSoup(r.content, "lxml")
    soup = soup.find("div", id="thumbnailsList")
    soup = soup.find_all('a', class_="_1B_yd")

    print(soup[3].get("href"))
    print(soup[5].get("href"))
  else:
    print("Request to Product Page != 200")




# change url and run
scrape(vans)
# 