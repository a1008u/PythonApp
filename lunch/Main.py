from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

'''
pip install selenium
brew install chromedriver ＊できないので、ローカルにdriverを保持
'''
browserChrome: WebDriver = webdriver.Firefox()
browserChrome.get('https://company.talknote.com/')

# login処理
elemUsername: WebElement = browserChrome.find_element_by_id('mail')
elemUsername.send_keys('a_uemoto@interspace.ne.jp')


elemPassword: WebElement = browserChrome.find_element_by_id('pass')
elemPassword.send_keys('us27CbED')


elemButton: WebElement = browserChrome.find_element_by_id('btn_login')
elemButton.click()


'''
検索
'''
sleep(3)
searchField: WebElement = browserChrome.find_element_by_id('search_field').find_element_by_tag_name('input')
searchField.send_keys('Have Fun Lunch')


'''
いいね取得 + csv抽出
'''
browserChrome\
    .find_element_by_class_name('goodcomment')\
    .find_element_by_class_name('like')\
    .click()


# いいねした人取得
popup: WebElement = browserChrome.find_element_by_class_name('member_popup')
bx: WebElement = popup.find_element_by_css_selector('.box_content')
liList: list = bx.find_elements_by_tag_name('li')
newList = [li.find_elements_by_tag_name('a')[1].text for li in liList]

# csv出力
with open('text2.csv', 'w') as f2:
    [f2.write(i + ',\n') for i in newList]


