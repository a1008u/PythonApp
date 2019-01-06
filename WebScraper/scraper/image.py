# PILの使い方

from PIL import Image

img = Image.open('python.png')
print(img.size)

# リサイズ
resizeImage = img.resize((500,300))
print(img.size, resizeImage.size)
resizeImage.save('reseizePython.png')

# siteから1枚の画像を収集する方法
import io
from urllib import request

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

browser: WebDriver = webdriver.Chrome('./chromedriver')
browser.get('https://scraping-for-beginner.herokuapp.com/image')

elem: WebElement = browser.find_element_by_class_name('material-placeholder')
elemTag: WebElement = elem.find_element_by_tag_name('img')
url: str = elemTag.get_attribute('src')
f = io.BytesIO(request.urlopen(url).read())
img = Image.open(f)
img.save('img01.jpg')

# siteから全てのの画像を収集する方法
elems: list = browser.find_elements_by_class_name('material-placeholder')

for index, elem in enumerate(elems):
    elemTag: WebElement = elem.find_element_by_tag_name('img')
    url: str = elemTag.get_attribute('src')
    f = io.BytesIO(request.urlopen(url).read())
    img = Image.open(f)
    img.save('../img/img{}.jpg'.format(index))

browser.quit()
