from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

browser: WebDriver = webdriver.Chrome('./chromedriver')
url: str ='https://transit.yahoo.co.jp/search/result' \
          '?flatlon=' \
          '&from={fromName}' \
          '&to={toName}' \
          '&viacode=' \
          '&via=' \
          '&viacode=' \
          '&via=' \
          '&viacode=' \
          '&via=' \
          '&y=2019' \
          '&m=01' \
          '&d=03' \
          '&hh=01' \
          '&m2=0' \
          '&m1=3' \
          '&type=1' \
          '&ticket=ic' \
          '&expkind=1' \
          '&ws=3' \
          '&s=0' \
          '&al=1' \
          '&shin=1' \
          '&ex=1' \
          '&hb=1' \
          '&lb=1' \
          '&sr=1' \
          '&kw=%E5%A4%A7%E5%AE%AE'.format(fromName='東京', toName='横浜')
browser.get(url)
