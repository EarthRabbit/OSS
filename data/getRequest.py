import requests
from bs4 import BeautifulSoup

def getRequest(address, selector):
    
    # 주소를 통해 웹 페이지 불러오기
    request = requests.get(address, headers={'User-Agent':'Mozilla/5.0'})
    assert request.status_code == 200

    # BeautifulSoup 모듈을 이용하여 사이트 정보를 DOM 형태로 변환
    dom = BeautifulSoup(request.content, 'html.parser')
    return dom.select(selector)