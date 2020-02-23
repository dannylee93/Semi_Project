# 셀레니움 드라이버 사용
from selenium import webdriver
import time

#이미지 검색 키워드 설정
keyword = 'twice'

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.implicitly_wait(30)

url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}'.format(keyword)
driver.get(url)

imgs = driver.find_elements_by_css_selector('img._img')
result = []
for img in imgs:
    if 'http' in img.get_attribute('src'):
        result.append(img.get_attribute('src'))
        
print(result)

driver.close()
print('수집완료')

import os
if not os.path.isdir('./{}'.format(keyword)):
    os.mkdir('./{}'.format(keyword))
    
#다운로드
from urllib.request import urlretrieve

for index, link in enumerate(result):
    start = link.rfind('.')
    end = link.rfind('&')
#     print(link[start:end])
    filetype = link[start:end]