from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import sys


'''
Main.exe 'アドレス' 'パスワード' '検索開始日(yyyy/mm/dd)' '検索完了日(yyyy/mm/dd)'
python Main.py 'アドレス' 'パスワード' '検索開始日(yyyy/mm/dd)' '検索完了日(yyyy/mm/dd)'
'''

for i in sys.argv:
    print("引数の出力 ", i)


'''
pip install selenium
brew install chromedriver ＊できないので、ローカルにdriverを保持
'''
browserChrome: WebDriver = webdriver.Firefox()
browserChrome.get('https://company.talknote.com/')

loginId: str = sys.argv[1]
passWord: str = sys.argv[2]


# login処理
elemUsername: WebElement = browserChrome.find_element_by_id('mail')
elemUsername.send_keys(loginId)


elemPassword: WebElement = browserChrome.find_element_by_id('pass')
elemPassword.send_keys(passWord)


elemButton: WebElement = browserChrome.find_element_by_id('btn_login')
elemButton.click()


'''
検索（検索ボックス入力 + 絞り込み）
'''
sleep(1)
searchField: WebElement = browserChrome.find_element_by_id('search_field').find_element_by_tag_name('input')
searchField.send_keys('Have Fun Lunch　参加者')

browserChrome.find_element_by_class_name('filter_button').click()

sleep(1)

startDate: str = sys.argv[3]
endDate: str = sys.argv[4]

browserChrome.find_element_by_id('top_item_filter_dialog')\
    .find_element_by_class_name('start_date_field')\
    .find_element_by_tag_name('input')\
    .send_keys(startDate)
browserChrome.find_element_by_id('top_item_filter_dialog')\
    .find_element_by_class_name('end_date_field')\
    .find_element_by_tag_name('input')\
    .send_keys(endDate)
browserChrome.find_element_by_id('filter_action_button').click()

sleep(2)


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
with open('participant.csv', 'w') as f2:
    [f2.write(i + ',\n') for i in newList]


