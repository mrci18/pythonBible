import requests
import bs4

res = requests.get('https://learncodeonline.in')
soup = bs4.BeautifulSoup(res.text, 'lxml')
hi = soup.select('title')
print(hi[0])
hi[0].getText()

res2 = requests.get('https://en.wikipedia.org/wiki/Naruto')
soup2 = bs4.BeautifulSoup(res2.text, 'lxml')

for i in soup2.select('div'):
    print(i.text)