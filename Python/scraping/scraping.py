import urllib.request
from bs4 import BeautifulSoup


datos = urllib.request.urlopen('http://www.2ionline.com').read().decode()
print(datos)

soup = BeautifulSoup(datos)

tags = soup('a')
for tag in tags:
    print(tag.get('href'))


