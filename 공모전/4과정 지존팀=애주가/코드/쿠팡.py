
from selenium import webdriver
import time
import re
from datetime import datetime
import pandas as pd



cafe_name = "쿠팡"

now = datetime.now()  # 파일이름 현 시간으로 저장하기
RESULT_PATH = 'C:/Users/wnstj/PycharmProjects/BigData/Crawling/'  # 결과 저장할 경로/파일명 (본인 경로로 수정)
outputFileName = cafe_name + '%s-%s-%s  %s시 %s분.csv' % (
    now.year, now.month, now.day, now.hour, now.minute)

def save_csv(RR):
    df = pd.DataFrame(RR)  # df로 변환
    df.to_csv(RESULT_PATH + outputFileName, mode='w')


def save(result):
    timestr = time.strftime("%Y%m%d-%H%M")

    dataWriteHandler = open(RESULT_PATH + cafe_name + timestr + ".txt", "w", encoding='utf-8')
    for items in result:
        print(items, file=dataWriteHandler)
    dataWriteHandler.close()


# 아래의 3줄은 해당 링크(url)을 chrome으로 열어라
driver = webdriver.Chrome("./chromedriver.exe")  # 돌리려는 .exe 파일의 위치(*변경*)
url = "https://www.coupang.com/vp/products/1372901?itemId=5920776&vendorItemId=3007587603&sourceType=SDP_BOUGHT_TOGETHER&isAddedCart="
# 테크 https://www.coupang.com/vp/products/141675?itemId=193467664&vendorItemId=4855258226&q=%ED%85%8C%ED%81%AC+%EC%95%A1%EC%B2%B4+%EC%84%B8%EC%A0%9C&itemsCount=36&searchId=92e29b75aa224aa5a1b2059f9cef8ad3&rank=5&isAddedCart=
# 열쇠고리 https://www.coupang.com/vp/products/177545760?itemId=507872206&vendorItemId=4302192234&q=%EC%97%B4%EC%87%A0%EA%B3%A0%EB%A6%AC&itemsCount=36&searchId=f30fb4f0a50445679b2a0cabeb40daf4&rank=3&isAddedCart=
# 저금통 https://www.coupang.com/vp/products/1372901?itemId=5920776&vendorItemId=3007587603&sourceType=SDP_BOUGHT_TOGETHER&isAddedCart=
# 열려고하는 페이지 링크 (현재는 테크 세제) (*변경*)
driver.get(url)

time.sleep(2)  # 만약에 에러뜨면 타임슬립 숫자 늘리기

# 상품평 클릭 #css_selector 부분이 html, css로 지정해서 그 부분을 클릭하라고 지시
driver.find_element_by_css_selector("#btfTab > ul.tab-titles > li:nth-child(2)").click()
# 만약 안돌아간다면 -> driver.find_element_by_css_selector("#btfTab.tab > ul.tab-titles > li:nth-child(2)").click() #html에 맞게 (*변경*)
time.sleep(2)

char = re.compile('[^ 0-9a-zA-Zㄱ-ㅣ가-힣!?#]')
page_lst_point = 1
coupang_riw = []
while True:
    # 본문 리스트 생성
    review_area = driver.find_element_by_class_name('sdp-review')
    review_list = review_area.find_elements_by_class_name(
        'sdp-review__article__list__review.js_reviewArticleContentContainer')
    time.sleep(1)
    # 버튼 리스트 생성
    try:
        Btn_area = review_area.find_element_by_class_name("sdp-review__article__page.js_reviewArticlePagingContainer")
        page_Btn_lst = Btn_area.find_elements_by_css_selector('button')

        next_page = page_lst_point + 2  # '2페이지'버튼 ~ '다음'버튼까지 클릭
        # page_Btn_lst[page_num+1]번째에 있는 버튼이 활성 상태인가?
        # 활성 상태이면 True, 비활성 상태이면 False를 반환
        next_Btn_state = page_Btn_lst[page_lst_point].is_enabled()
    # 예외처리 - sdp-review__article__page.js_reviewArticlePagingContainer 이 없을 때
    except:
        print(" [예외 발생] 페이지네이션 없음 ")

    # 페이지내 정보 추출 (본문)------------------------------------------------------
    review_list = review_area.find_elements_by_class_name(
        'sdp-review__article__list__review.js_reviewArticleContentContainer')
    for riw in review_list:
        comment = riw.text
        comment = str(comment)
        comment = char.sub('', comment)
        coupang_riw.append(comment)
    # --------------------------------------------------------------------------#

    if (next_Btn_state == True):
        driver.find_element_by_css_selector(
            "#btfTab > ul.tab-contents > li.product-review > div > div.sdp-review__article.js_reviewArticleContainer > section.js_reviewArticleListContainer > div.sdp-review__article__page.js_reviewArticlePagingContainer > button:nth-child(" + str(
                next_page) + ")").click()
        time.sleep(2)
    else:
        print("완료")
        break
    if (next_page == 12):
        page_lst_point = 1
    else:
        page_lst_point += 1
save_csv(coupang_riw)
save(coupang_riw)
driver.close()

