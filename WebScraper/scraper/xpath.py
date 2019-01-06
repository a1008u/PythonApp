from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

browser: WebDriver = webdriver.Chrome('./chromedriver')
browser.get('https://scraping-for-beginner.herokuapp.com/')


elemXpath = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/ul/li[1]')
_, text = elemXpath.text.split(' ')
print(text)


browser.quit()
