
# melon DJ 크롤링 코드
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 크롬드라이버를 설치한 경로 chromedriver.exe가 존재하는 path를 지정합니다.
webdriver_path = 'chromedriver'

# Chrome WebDriver 실행
browser = webdriver.Chrome(webdriver_path)

# 멜론 DJ 우울 플레이리스트 중 첫번째 플리의 url을 가져왔습니다.
url = "https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=478102836"

browser.implicitly_wait(3)

browser.get(url)  # 페이지 접속

song_name_ls=[]

singer_ls=[]

lyrics_ls =[]

genre_ls=[]

cover_Is=[]

ytLink_ls=[]

from selenium.common.exceptions import NoSuchElementException


browser.implicitly_wait(3)
browser.get(url)  # 페이지 접속

song_num =1 # 1페이지의 1번노래부터, 이변수는 페이지를 넘어가기 위한 변수입니다.

page_number = 3 # 이 값은 몇 페이지까지 크롤링할것인지 정해주는 부분으로써, 유동적으로 변경한다.


for page in range(1,page_number+1):
    print(f"page {page} : ")
    
    # 크롤링 코드
    for i in range(1,50+1): # 한페이지당 50개의 음악이 존재한다.
        
        browser.execute_script("document.body.style.zoom='2%'") #화면 배율을 최대한 낮게하면 한화면에 모든 요소를 볼 수 있다.
        
        browser.implicitly_wait(3) # 대기시간 부여하는 코드
        
        search_button = browser.find_element(By.XPATH ,f'//*[@id="frm"]/div/table/tbody/tr[{i}]/td[4]/div/a') #음원정보로 연결되는 링크의 xpath이다.

        browser.implicitly_wait(1)

        search_button.send_keys(Keys.ENTER) # 위에서 찾은 음원의 정보페이지로 넘어가기(엔터키)


        browser.implicitly_wait(2)

        browser.execute_script("document.body.style.zoom='2%'") # 음원정보 페이지에서도 마찬가지로 배율 줄이기

        song_name=browser.find_element(By.XPATH ,'//*[@id="downloadfrm"]/div/div/div[2]/div[1]/div[1]') # 노래제목

        singer=browser.find_element(By.XPATH ,'//*[@id="downloadfrm"]/div/div/div[2]/div[1]/div[2]/a/span[1]') #가수명
        print(singer)

        genre=browser.find_element(By.XPATH ,'//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]') # 장르
        
        #앨범커버
        cover=browser.find_element(By.XPATH ,'//*[@id="downloadfrm"]/div/div/div[1]/a/img').get_attribute('src')
        
        
        
        try: #가사 정보가 없는 노래들에대한 예외처리
            search_button = browser.find_element(By.XPATH ,'//*[@id="lyricArea"]/button') 
            # 가사는 반으로 접혀있기때문에 더보기 버튼 찾기

            search_button.send_keys(Keys.ENTER) # 더보기 클릭
            
            lyrics_element = browser.find_element(By.XPATH, '//*[@id="d_video_summary"]')
            
            lyrics = lyrics_element.text
            
            
        except NoSuchElementException: # find_element에서 exception 발생하면 공백처리시켜주기
            lyrics =" "

        link="https://www.youtube.com/results?search_query="+singer.text+"+"+song_name.text # youtube 검색 링크
        
        song_name_ls.append(song_name.text) # 각리스트에 저장

        singer_ls.append(singer.text)

        genre_ls.append(genre.text)

        lyrics_ls.append(lyrics)
        
        cover_Is.append(cover)
        ytLink_ls.append(link)

        print(i," : ",song_name.text,singer.text, cover)

        
        browser.get(url)  # 기존페이지로 이동
        
        browser.implicitly_wait(3)

    
    song_num+= (50) # 다음 페이지로 넘어가기위해 50개씩 1부터 시작되므로 1,51,101,151 ... 이런식으로 시작index가 존재한다.
    url = f"https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=478102836#params%5BplylstSeq%5D=478102836&po=pageObj&startIndex={song_num}"
    #url마지막의 startIndex를 통해 페이지를 넘어가도록 하였다.

    browser.get(url)  # 다음페이지로 이동하기
    
    
    browser.implicitly_wait(3)