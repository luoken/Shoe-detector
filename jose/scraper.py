import requests
import lxml
import urllib
from bs4 import BeautifulSoup


adidas = "https://www.zappos.com/adidas-men-shoes/CK_XAVoBAcABAuICAwELGA.zso"
nike = "https://www.zappos.com/nike-men-shoes/CK_XAVoBb8ABAuICAwELGA.zso"
vans =   "https://www.zappos.com/vans-men-shoes/CK_XAVoCqwHAAQLiAgMBCxg.zso"

def saveImg(url, name):
  urllib.urlretrieve(url, name)


def scrape(url, limit):
  r = requests.get(url)
  productLinks = []
  pageList = []

  if(r.status_code == 200):
    soup = BeautifulSoup(r.content, "lxml")
    productLinks = soup.find_all("a", class_='product')

    for i in productLinks:
      pageList.append(i.get('href'))

    if 'adidas' in url:
      brandName = 'adidas'
    elif 'nike' in url:
      brandName = 'nike'
    else:
      brandName = 'vans'

    # for i in range(len(pageList)):
    for i in range(limit):
      url = pageList[i]
      scrapeProductPage("https://www.zappos.com" + url, brandName, i)
  else:
    print("Error: Response Status Code != 200")
    print("Error: Ask Jose why it broke.")


def scrapeProductPage(url, brandName, i):
  r = requests.get(url)

  if(r.status_code == 200):
    soup = BeautifulSoup(r.content, "lxml")
    soup = soup.find("div", id="thumbnailsList")
    soup = soup.find_all('a', class_="_1B_yd")

    saveImg(soup[0].get("href"), brandName + "-both-" + str(i) + ".jpg")
    saveImg(soup[3].get("href"), brandName + "-outside-"+ str(i) + ".jpg")
    saveImg(soup[5].get("href"), brandName + "-inside-" + str(i) + ".jpg")
  else:
    print("Request to Product Page != 200")


# change url and run
def scrapeZappos(n, limit):
  for i in range(n):
    print("Scraping from: " + vans + "?p=" + str(i))
    scrape(vans + "?p=" + str(i), limit)
  for i in range(n):
    print("Scraping from: " + adidas + "?p=" + str(i))
    scrape(adidas + "?p=" + str(i), limit)
  for i in range(n):
    print("Scraping from: " + nike + "?p=" + str(i))
    scrape(nike + "?p=" + str(i), limit)
# (# pages, # shoes per page)
scrapeZappos(1, 10);