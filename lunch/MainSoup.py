# from bs4 import BeautifulSoup
# import requests
#
# html = requests.get('https://company.talknote.com/')
# soup: BeautifulSoup = BeautifulSoup(html.text, 'lxml')
#
# titles = soup.find_all('title')
# print(titles[0].text)
#
# mail = soup.find(id="mail")
# print('mail : ', mail)
# text = mail.get('value')
# print(text)
# text = 'tttt'
# print(mail.get('value'))
#
# metas: list = soup.find_all('meta')
# print(len(metas))
# for meta in metas:
#     print(meta)

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://company.talknote.com/'
html = urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')
# soup = BeautifulSoup(html, 'html5lib')

# prettifyで整形されたファイルで保存
with open('test.html', mode = 'w', encoding = 'utf-8') as fw:
    fw.write(soup.prettify())
