import requests
import lxml
import urllib
from bs4 import BeautifulSoup

adidasUrl = "https://www.zappos.com/adidas-men-shoes/CK_XAVoBAcABAuICAwELGA.zso"
nikeUrl = "https://www.zappos.com/nike-men-shoes/CK_XAVoBb8ABAuICAwELGA.zso"
vansUrl =   "https://www.zappos.com/vans-men-shoes/CK_XAVoCqwHAAQLiAgMBCxg.zso"

def saveImg(url, brand, n):
  name = brand + '-'  +  str(n) + '.jpg'
  urllib.urlretrieve(url, name)

def scrape(url):
  r = requests.get(url)
  imgSrcUrls = []

  if(r.status_code == 200):
    soup = BeautifulSoup(r.content, "lxml")
    imgSrcList = soup.find_all("img", class_='productImg')
    srcList = []

    for i in imgSrcList:
      srcList.append(i.get('src'))

    for i in range(10):
      brandName = ''
      if "http" in srcList[i]:
        if 'adidas' in url:
          brandName = 'adidas'
        elif 'nike' in url:
          brandName = 'nike'
        else:
          brandName = 'vans'
        saveImg(srcList[i], brandName, i)
  else:
    print("Error: Response Status Code != 200")

# change url and run
scrape(vansUrl)
