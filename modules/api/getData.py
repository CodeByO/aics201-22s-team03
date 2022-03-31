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
    
    def getApi(self,date):
        params = {'serviceKey': self.api_key, 'LAWD_CD' : '36110','DEAL_YMD':date}
        response = requests.get(self.url,params=params).content
        
        xmlData = xmltodict.parse(response)

        header = xmlData['response']['header']
        items = xmlData['response']['body']['items']
        resultCode = header['resultCode']

        if resultCode != '00':
            resultMsg = header['resultMsg']
            print("API 요청 에러 발생 resultCode : " + resultCode)
            print("------------------------------------")
            print(resultMsg)
            print("------------------------------------")
            return None 
        elif items == None:
            print("API 요청 에러 발생")
            print("------------------------------------")
            print("해당 하는 데이터가 없음")
            print("------------------------------------")
            return None
        item = items['item']
        print(item[0]["건축년도"])
        
        # test = item['지역코드']['법정동']['계약면적']['월세금액']['보증금액']['건축년도']
        data = []
        tmp = []
        for i in range(len(item)):
            tmp = []
            
            tmp.append(item[i]['지역코드'])
            tmp.append(item[i]['법정동'])
            tmp.append(item[i]['계약면적'])
            tmp.append(item[i]['월세금액'])
            tmp.append(item[i]['보증금액'])
            tmp.append(item[i].get('건축년도','0000'))
            
            data.append(tmp)
        
        return data