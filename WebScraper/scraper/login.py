from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

browser: WebDriver = webdriver.Chrome('./chromedriver')
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')



# login処理
elemUsername: WebElement = browser.find_element_by_id('username')
elemUsername.send_keys('imanishi')


elemPassword: WebElement = browser.find_element_by_id('password')
elemPassword.send_keys('kohei')


elemButton: WebElement = browser.find_element_by_id('login-btn')
elemButton.click()

# テキストデータ取得
elemName: WebElement = browser.find_element_by_id('name')
print('名前 ： ', elemName.text)

elemCompany: WebElement = browser.find_element_by_id('company')
print('所属企業 ： ', elemCompany.text)

elemBirthday: WebElement = browser.find_element_by_id('birthday')
print('生年月日 ： ', elemBirthday.text)

elemComeForm: WebElement = browser.find_element_by_id('come_from')
print('出身 ： ', elemComeForm.text)

elemHobby: WebElement = browser.find_element_by_id('hobby')
print('趣味 ： ', elemHobby.text.replace('\n', ' '))

elemsTh: list = browser.find_elements_by_tag_name('th')
elemsThList: list = [elemth.text for elemth in elemsTh]
print(elemsThList)

elemsValue: list = browser.find_elements_by_tag_name('td')
elemsValueList: list = [elemValue.text for elemValue in elemsValue]
print(elemsValueList)


# csv出力
import pandas
dataFrame: pandas.DataFrame = pandas.DataFrame()
dataFrame['key'] = elemsThList
dataFrame['value'] = elemsValueList

print(dataFrame)
dataFrame.to_csv('講師情報.csv', index=False)

# browser.quit()





