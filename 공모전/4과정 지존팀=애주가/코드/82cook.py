import re
from selenium import webdriver
import bs4
from time import sleep
from datetime import datetime
import pandas as pd




URL = []

key = input("검색어 입력")
max_page = input("페이지 입력")


now = datetime.now()  # 파일이름 현 시간으로 저장하기
RESULT_PATH = 'C:/Users/wnstj/PycharmProjects/BD/crwa/'  # 결과 저장할 경로/파일명 (본인 경로로 수정)
outputFileName = "82cook" + key + '%s-%s-%s  %s시 %s분.csv' % (
    now.year, now.month, now.day, now.hour, now.minute)

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)


def save_csv(RR):
    df = pd.DataFrame(RR)  # df로 변환
    df.columns = ["Date", "Title", "Contents", "Comments"]
    df.to_csv(RESULT_PATH + outputFileName, mode='w')


for page in range(1, (int(max_page) + 1)):
    url = 'https://www.82cook.com/entiz/enti.php?bn=15&searchType=search&search1=1&keys=' + key + '&page=' + str(page)
    driver.get(url)

    x = 1
    while(x <= 25):
        url_list = driver.find_elements_by_css_selector('#bbs > table > tbody > tr:nth-child('+ str(x) +') > td.title > a')
        x = x + 1
        for uu in url_list:
            URL.append(uu.get_attribute('href'))

all = []
for i in URL:
    result = []
    driver.get(i)
    soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')

    date = soup.findAll('div', {'class': 'readRight'})
    for de in date:
        result.append(de.text)

    title = soup.findAll('h4', {'class':'title bbstitle'})
    for ti in title:
        result.append(ti.text)

    body = soup.findAll('div', {'id': 'articleBody'})
    for bo in body:
        result.append(bo.text.replace("\n", ""))

    comment = soup.find_all('ul', {'class': 'reples'})
    for n in range(0, len(comment)):
        comment[n] = comment[n].get_text().replace("\n", "")
    result.append(comment)

    all.append(result)

save_csv(all)


