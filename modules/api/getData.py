import requests
import os


from dotenv import load_dotenv

load_dotenv(verbose=True)

#[Function] Open API 데이터 호출
#[DESC] 지역코드와 날짜를 인자로 받아 Open API의 데이터 조회
#[TODO] 인자 세팅

class getData:
    
    def __init__(self):
        api_key = os.getenv('API_KEY')
        url = os.getenv('API_URL')
    
    def getApi(self):
        params = {'serviceKey': self.api_key, 'LAWD_CD' : '11110','DEAL_YMD':'2021312'}
        response = requests.get(self.url,params=params)
        return response