import requests
import os
from dotenv import load_dotenv
import xmltodict
from datetime import datetime

load_dotenv(verbose=True)

#[Function] Open API 데이터 호출
#[DESC] 지역코드와 날짜를 인자로 받아 Open API의 데이터 조회
#[TODO] 딕셔너리 -> 리스트 화

class getData:
    
    def __init__(self):
        api_key = os.getenv('API_KEY')
        self.api_key = requests.utils.unquote(api_key)
        self.url = os.getenv('API_URL')
        self.date = datetime.today().strftime("%Y%m")
    
    def getApi(self):
        params = {'serviceKey': self.api_key, 'LAWD_CD' : '36110','DEAL_YMD':self.date}
        response = requests.get(self.url,params=params).content
        
        xmlData = xmltodict.parse(response)

        header = xmlData['response']['header']
        resultCode = header['resultCode']

        if resultCode != '00':
            resultMsg = header['resultMsg']
            print("API 요청 에러 발생 resultCode : " + resultCode)
            print("------------------------------------")
            print(resultMsg)
            print("------------------------------------")
            return None
        

        item = xmlData['response']['body']['items']['item']
        # data = item['지역코드']['법정동']['계약면적']['월세금액']['보증금액']['건축년도']
        
        return item