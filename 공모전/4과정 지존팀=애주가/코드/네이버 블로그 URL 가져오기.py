import re
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import pandas as pd
from konlpy.tag import Okt
from selenium.common.exceptions import TimeoutException
import bs4

query = input("검색어 입력")
max_page = input("페이지 입력")
t = Okt()
source = "네이버 블로그"

now = datetime.now()  # 파일이름 현 시간으로 저장하기
RESULT_PATH = 'C:/Users/wnstj/PycharmProjects/BigData/Crawling/'  # 결과 저장할 경로/파일명 (본인 경로로 수정)
outputFileName = query + '%s-%s-%s  %s시 %s분.csv' % (
    now.year, now.month, now.day, now.hour, now.minute)

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)

def clean_text(text_in_file):
    text_in_file_1th = re.sub('[a-zA-Z]', '', text_in_file)
    text_in_file_2th = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', '', text_in_file_1th)

    return text_in_file_2th


def save_csv(RR):
    try:
        df = pd.DataFrame(RR)  # df로 변환
        df.columns = ["Keyword", "Contents", "Words", "Source", "URL"]
        df.to_csv(RESULT_PATH + outputFileName, mode='w')
    except:
        df = pd.DataFrame(RR)  # df로 변환
        df.columns = ["URL"]
        df.to_csv(RESULT_PATH + '블로그 URL 리스트' + outputFileName, mode='w')


# 네이버에 키워드 검색
def get_url():

    pn = 1
    maxpage_t = (int(max_page) - 1) * 10 + 1
    url_list = []

    # while문을 사용해서 최대 페이지 수만큼 크롤링 먼저 네이버 검색 url 가져와서 검색어, 페이지 번호 붙여서 웹드라이버로 이동
    # try:
    while (pn <= int(maxpage_t)):
        naver_url = "https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1" \
                    "&nso=&post_blogurl=&post_blogurl_without=&query=" + query + \
                    "&sm=tab_pge&srchby=all&st=sim&where=post&start=" + str(pn)
        driver.get(naver_url)
        # print(naver_url)

        pn = pn + 10
        i = 1
        while (i <= 10):
            current_url = driver.find_elements_by_xpath('//*[@id="sp_blog_'+str(i)+'"]/dl/dt/a')
            for li in current_url:
                url_li = li.get_attribute('href')
                url_list.append(url_li)
            i = i + 1
    save_csv(url_list)
    # except:
    #     print('err')


if __name__ == '__main__':
    get_url()
