from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.com/imghp?hl=ko&ogbl") #사이트 접속

elem = driver.find_element_by_name("q") #검색창 
elem.send_keys("김선호") #입력

elem.send_keys(Keys.RETURN) #엔터키

time.sleep(1)
images = driver.find_elements_by_css_selector("img[class='YQ4gaf']")    #여러장 접속은 elements사용,class를 사용하자
count = 308
for image in images:
    try:
        image.click()
        time.sleep(1.3)
        imgurl = driver.find_element_by_css_selector(".sFlh5c.FyHeAf.iPVvYb").get_attribute("src")  #이미지 주소에 접속
        time.sleep(1.3)
        opener=urllib.request.build_opener()    #3줄 : 다운로드 차단을 뚫는 코드
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imgurl,str(count)+"test.jpg")  #주소를 변수에 담고 다운로드, 사진파일 이름
        count = count + 1    #사진저장을 위한 숫자표시
    except:
        pass
driver.close()

# SCROLL_PAUSE_TIME = 2

# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight") #브라우저의 높이를 구해 변수에 저장

# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #

#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height




# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()