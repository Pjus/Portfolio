import re
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import pandas as pd
from konlpy.tag import Okt

query = input("검색어 입력")
max_page = input("페이지 입력")
t = Okt()
source = "네이버 블로그"

now = datetime.now()  # 파일이름 현 시간으로 저장하기
RESULT_PATH = 'C:/Users/wnstj/PycharmProjects/BD/crwa/'  # 결과 저장할 경로/파일명 (본인 경로로 수정)
outputFileName = query + '%s-%s-%s  %s시 %s분.csv' % (
    now.year, now.month, now.day, now.hour, now.minute)

# 데이터 깔끔하게 만들기
def clean_text(text_in_file):
    text_in_file_1th = re.sub('[a-zA-Z]', '', text_in_file)
    text_in_file_2th = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', '', text_in_file_1th)

    return text_in_file_2th


def save_txt(result):
    RESULT_PATH = 'C:/Users/wnstj/PycharmProjects/BD/crwa/'  # 결과 저장할 경로/파일명 (본인 경로로 수정)
    timestr = time.strftime("%Y%m%d-%H%M%S")

    dataWriteHandler = open(RESULT_PATH + timestr + ".txt", "w", encoding='utf-8')
    for items in result:
        print(items, file=dataWriteHandler)
    dataWriteHandler.close()


def save_csv(RR):
    print(RR)
    df = pd.DataFrame(RR)  # df로 변환
    df.columns = ["Keyword", "Date", "Title", "Contents", "Words", "Source", "URL"]
    df.to_csv(RESULT_PATH + outputFileName, mode='w')

# 네이버에 키워드 검색
def get_url():
    # 아이디 비밀번호 검색어 페이지 인풋으로 입력
    # id = input("아이디를 입력하세요")
    # pw = input("비밀번호를 입력하세요")

    # 크롬드라이버 사용 본인 경로 확인, 위에서 선언한 크롬 옵션 사용
    driver = webdriver.Chrome('./chromedriver')
    driver.implicitly_wait(3)

    pn = 1
    maxpage_t = (int(max_page) - 1) * 10 + 1
    all = []

    # while문을 사용해서 최대 페이지 수만큼 크롤링 먼저 네이버 검색 url 가져와서 검색어, 페이지 번호 붙여서 웹드라이버로 이동

    while (pn <= int(maxpage_t)):
        naver_url = "https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1" \
                    "&nso=&post_blogurl=&post_blogurl_without=&query=" + query + \
                    "&sm=tab_pge&srchby=all&st=sim&where=post&start=" + str(pn)
        driver.get(naver_url)
        # print(naver_url)

        pn = pn + 10

        i = 1

        while (i <= 10):
            """
            #sp_blog_1 > dl > dt > a
            """
            list_url = driver.find_elements_by_css_selector('#sp_blog_'+ str(i) +' > dl > dt > a')
            sleep(2)

            for link in list_url:
                link.click()
            sleep(1)

            driver.switch_to.window(driver.window_handles[1])
            sleep(1)
            # c = driver.current_url
            # print(c)
            try:
                driver.switch_to.frame('mainFrame')
            except:
                pass
            try:
                driver.switch_to.frame('hiddenFrame')
            except:
                pass
            try:
                driver.switch_to.frame('screenFrame')
            except:
                pass

            body_list = [query]

            current_url = driver.current_url

            tbody = driver.find_elements_by_class_name('se-main-container')
            b_title = driver.find_elements_by_css_selector('#SE-83244aa0-a12b-11e9-a159-3320229c3479')
            date = driver.find_elements_by_xpath('//*[@id="SE-afb73716-f6a5-47e5-bf02-a900c35773e4"]/div/div/div[3]/span[2]')
            for da in date:
                ddate = da.text
                body_list.append(ddate)
            for tit in b_title:
                title = tit.text
                body_list.append(title)
            for txt in tbody:
                body = txt.text
                body_list.append(clean_text(body).replace("\n", ""))
                word = t.nouns(body)
                word = str(word).strip('[]')
                body_list.append(word)
            body_list.append(source)
            body_list.append(current_url)
            all.append(body_list)
            driver.close()
            sleep(2)
            driver.switch_to.window(driver.window_handles[0])
            i = i + 1
    for i in all:
        print(i)
    save_csv(all)

        # 드라이버 종료
    driver.close()

if __name__ == '__main__':
    get_url()
