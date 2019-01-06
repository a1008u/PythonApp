from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

browser: WebDriver = webdriver.Chrome('./chromedriver')
browser.get('https://scraping-for-beginner.herokuapp.com/ranking/')

elemRankingBox: WebElement = browser.find_element_by_class_name('u_areaListRankingBox')
elemTitle: WebElement = elemRankingBox\
    .find_element_by_class_name('u_title')\
    .find_element_by_tag_name('h2')
titles: str = elemTitle.text
_, title = titles.split('\n')
print(title)

# 総合評価
elemRankBox: WebElement = browser.find_element_by_class_name('u_rankBox')
elemSumRank: WebElement = elemRankBox.find_element_by_class_name('evaluateNumber')
print('総合ランク ', elemSumRank.text)

# 他の評価
elemAnotherRankBox: WebElement = browser.find_element_by_class_name('u_categoryTipsItem')
elemRankHobby: WebElement = elemAnotherRankBox.find_elements_by_class_name('is_rank')[0]
elemHbyRank: WebElement = elemRankHobby.find_element_by_class_name('evaluateNumber')
print('楽しさ : ', elemHbyRank.text)


elemPeople: WebElement = elemAnotherRankBox.find_elements_by_class_name('is_rank')[1]
elemPle: WebElement = elemPeople.find_element_by_class_name('evaluateNumber')
print('人混みの多さ : ', elemPle.text)


elemRankView: WebElement = elemAnotherRankBox.find_elements_by_class_name('is_rank')[2]
elemView: WebElement = elemRankView.find_element_by_class_name('evaluateNumber')
print('景色 : ', elemView.text)


elemRankAcc: WebElement = elemAnotherRankBox.find_elements_by_class_name('is_rank')[3]
elemAcc: WebElement = elemRankAcc.find_element_by_class_name('evaluateNumber')
print('アクセス : ', elemAcc.text)

# 全ての情報取得(タイトル)
elemRankingBs: list = browser.find_elements_by_class_name('u_areaListRankingBox')

titleList: list = []
for elemRankB in elemRankingBs:
    elemTitle: WebElement = elemRankB.find_element_by_class_name('u_title')
    titleSplit = elemTitle.text.split('\n')[1]

    titleList.append(titleSplit)

print(titleList)

# 全ての情報取得(総合評価)
elemRankingBs: list = browser.find_elements_by_class_name('u_areaListRankingBox')

sumRankingList: list = []
for elemRankB in elemRankingBs:
    elemRanking: WebElement = elemRankB.find_element_by_class_name('u_rankBox')
    elemSumRank: WebElement = elemRanking.find_element_by_class_name('evaluateNumber')
    rank: float = float(elemSumRank.text)
    sumRankingList.append(rank)

print(sumRankingList)


# 全ての情報取得(各評価)
elemRankingBs: list = browser.find_elements_by_class_name('u_areaListRankingBox')

rankingList: list = []
for elemRankB in elemRankingBs:
    elemAnotherRankBox: WebElement = elemRankB.find_element_by_class_name('u_categoryTipsItem')
    elemAnotherRanks: list = elemAnotherRankBox.find_elements_by_class_name('is_rank')
    tempRankingList: list = [float(elemAnotherRb.find_element_by_class_name('evaluateNumber').text) for elemAnotherRb in elemAnotherRanks]
    rankingList.append(tempRankingList)

print(rankingList)

# Pandasに変換
import pandas

dataFrame1: pandas.DataFrame = pandas.DataFrame()
dataFrame1['観光地名'] = titleList
dataFrame1['総合評価'] = sumRankingList
print(dataFrame1)

dataFrame2: pandas.DataFrame = pandas.DataFrame(rankingList)
dataFrame2.columns = ['楽しさ', '人混みの多さ', '景色', 'アクセス']
print(dataFrame2)

concatDataFrame: pandas.DataFrame = pandas.concat([dataFrame1, dataFrame2], axis=1)
print(concatDataFrame)
concatDataFrame.to_csv('観光地情報.csv', index=False)


# 全ページの情報取得

ts: list = []
srs: list = []
rs: list = []
for page in range(1, 4):
    browser.get('https://scraping-for-beginner.herokuapp.com/ranking/?page={}'.format(page))

    elemRankingBs: list = browser.find_elements_by_class_name('u_areaListRankingBox')
    for elemRankB in elemRankingBs:
        elemTitle: WebElement = elemRankB.find_element_by_class_name('u_title')
        titleSplit = elemTitle.text.split('\n')[1]
        ts.append(titleSplit)

    for elemRankB in elemRankingBs:
        elemRanking: WebElement = elemRankB.find_element_by_class_name('u_rankBox')
        elemSumRank: WebElement = elemRanking.find_element_by_class_name('evaluateNumber')
        rank: float = float(elemSumRank.text)
        srs.append(rank)

    for elemRankB in elemRankingBs:
        elemAnotherRankBox: WebElement = elemRankB.find_element_by_class_name('u_categoryTipsItem')
        elemAnotherRanks: list = elemAnotherRankBox.find_elements_by_class_name('is_rank')
        tempRankingList: list = [float(elemAnotherRb.find_element_by_class_name('evaluateNumber').text) for elemAnotherRb in elemAnotherRanks]
        rs.append(tempRankingList)


print('タイトル ', ts)
print('総合ランキング ', srs)
print('項目別ランキング ', rs)

# Pandasに変換
import pandas

dataFrame3: pandas.DataFrame = pandas.DataFrame()
dataFrame3['観光地名'] = ts
dataFrame3['総合評価'] = srs
print(dataFrame3)

dataFrame4: pandas.DataFrame = pandas.DataFrame(rs)
dataFrame4.columns = ['楽しさ', '人混みの多さ', '景色', 'アクセス']
print(dataFrame4)

concatDataFrame: pandas.DataFrame = pandas.concat([dataFrame3, dataFrame4], axis=1)
print(concatDataFrame)
concatDataFrame.to_csv('観光地総合情報.csv', index=False)


browser.quit()





