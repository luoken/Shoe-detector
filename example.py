import requests
from bs4 import BeautifulSoup

#my url
url = 'https://www.shopwss.com/mens-shoes/all-mens-shoes.htm?sort=S#pageSize=144'

#getting the page with the url
page = requests.get(url)

#beautiful soup will grab everything
soup = BeautifulSoup(page.text, 'html5lib')

a_tags_pi = soup.find_all('a', class_ = 'pi-link')


print(a_tags_pi[0])
print(len(a_tags_pi))

img_lazy = soup.find_all('img', class_= 'pi-img lazy')
for i in img_lazy:
    print(i)
    print('\n')

print(len(img_lazy))
