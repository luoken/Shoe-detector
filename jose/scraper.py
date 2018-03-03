import requests
import lxml
import urllib
from bs4 import BeautifulSoup


adidas = "https://www.zappos.com/men-shoes/CK_XAVoHAdIG4QbsHMABAuICAwELGA.zso"
nike = "https://www.zappos.com/nike-men-shoes/CK_XAVoBb8ABAuICAwELGA.zso"
vans =   "https://www.zappos.com/vans-men-shoes/CK_XAVoCqwHAAQLiAgMBCxg.zso"


def saveImg(url, name):
  urllib.urlretrieve(url, "./images/" + name)



def scrape(url, limit, counter):

  r = requests.get(url)
  productLinks = []
  pageList = []

  if(r.status_code == 200):
    soup = BeautifulSoup(r.content, "lxml")
    productLinks = soup.find_all("a", class_='product')

    for i in productLinks:
      pageList.append(i.get('href'))

    if 'vans' in url:
      brandName = 'vans'
    elif 'nike' in url:
      brandName = 'nike'
    else:
      brandName = 'adidas'

    # Verify limit is within bounds
    if limit > 100:
      limit = 100
      print("Can't scrape more than 100 items per page")
      print("Scraping for 100 items per page")
    
    if limit <= 0:
      print("Can't scrape negative number of shoes")
      print("Enter a number >= 1")
      return

    if limit > len(pageList):
      limit = len(pageList)
      print("Couldn't scrape " + str(limit) + " items")
      print("There are only " + str(len(pageList)) + " items available to scrape on this page")
    

    for i in range(limit):
      url = pageList[i]
      scrapeProductPage("https://www.zappos.com" + url, brandName, counter, i)

  else:
    print("Error: Response Status Code != 200")
    print("Error: Ask Jose why it broke.")


def scrapeProductPage(url, brandName, ctr, i):
  r = requests.get(url)

  if(r.status_code == 200):
    soup = BeautifulSoup(r.content, "lxml")
    soup = soup.find("div", id="thumbnailsList")
    soup = soup.find_all('a', class_="_1B_yd")

    saveImg(soup[0].get("href"), brandName + "-both-" + str(ctr) +  str(i) + ".jpg")
    saveImg(soup[3].get("href"), brandName + "-outside-"+ str(ctr) + str(i) + ".jpg")
    saveImg(soup[5].get("href"), brandName + "-inside-" + str(ctr) + str(i) + ".jpg")
  else:
    print("Request to Product Page != 200")

# change url and run
def scrapeZappos(n, limit):
  counter = 0
  for i in range(n):
    print("Scraping from: " + vans + "?p=" + str(i))
    scrape(vans + "?p=" + str(i), limit, counter)
    counter = counter + 1
  counter = 0
  for i in range(n):
    print("Scraping from: " + adidas + "?p=" + str(i))
    scrape(adidas + "?p=" + str(i), limit, counter)
    counter = counter + 1
  counter = 0
  for i in range(n):
    print("Scraping from: " + nike + "?p=" + str(i))
    scrape(nike + "?p=" + str(i), limit, counter)
    counter = counter + 1
  counter = 0
  
# (# pages, # shoes per page)
scrapeZappos(3, 100);