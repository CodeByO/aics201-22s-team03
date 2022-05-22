
import requests
import os
from dotenv import load_dotenv
import xmltodict
import csv
from datetime import datetime

nowDate = datetime.today().strftime("%Y%m")
sejong = '36110'
load_dotenv(verbose=True)
fpath = os.path.dirname(os.path.abspath(__file__))

#[Function] Open API 데이터 호출
#[DESC] 지역코드와 날짜를 인자로 받아 Open API의 데이터 조회
#[TODO] 요청 받은 데이터를 재가공해서 파일로 저장


class getData:
    
    def __init__(self):
        api_key = os.getenv('API_KEY')
        self.api_key = requests.utils.unquote(api_key)
        self.url = os.getenv('API_URL')
    
    def getApi(self,date=nowDate,locate=sejong):
        params = {'serviceKey': self.api_key, 'LAWD_CD' : locate,'DEAL_YMD':date}
        response = None
        try:
            response = requests.get(self.url,params=params).content
        except requests.exceptions.Timeout as errd:
            print("타임아웃 에러 : ", errd)
        except requests.exceptions.ConnectionError as errc:
            print("연결 에러 : ", errc)
    
        
        xmlData = xmltodict.parse(response)

        header = xmlData['response']['header']
        resultCode = header['resultCode']
        items = None
        try:
            items = xmlData['response']['body']['items']
        except:
            pass

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
        self.dictToList(items['item'],date,locate)
        
    def dictToList(self,item,date,locate):
        data = []

        for i in range(len(item)):
            tmp = []
            
            tmp.append(self.findLocal(item[i]['지역코드']))
            tmp.append(item[i]['법정동'])
            tmp.append(item[i]['계약면적'])
            tmp.append(item[i]['월세금액'])

            tmp.append(item[i]['보증금액'].replace(",",""))
            tmp.append(item[i].get('건축년도','0000'))
            
            data.append(tmp)
        #api 요청 한것을 파일로 저장
        with open(fpath + '/roomList.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(date)
            writer.writerow(locate)
            writer.writerows(data)

        

    def findLocal(self,target):
        with open(fpath + '/regionCode.csv','r',encoding='UTF-8') as file:
    
            reader = csv.reader(file)
            match = [s for s in reader if target in s] 
            if match == []:
                return None
                
        return match[0][0]


    def devideRoom(self,date=nowDate,locate=sejong):
        self.checkFile(date,locate)
        count = 0
        try:
            with open(fpath + '/roomList.csv','r',encoding='UTF-8') as file:
                
                roomList = csv.reader(file)
                monthly = []
                
                charter = []

                for i in roomList:
                    count += 1
                    if count > 2:

                        if i[3] == '0':
                            charter.append(i)
                        else:
                            monthly.append(i)
        
            return monthly, charter
        except Exception as error:
            print("파일 처리 에러 발생",error)
    
    def checkFile(self,date=nowDate,locate=sejong):
        count = 0

        if os.path.isfile(fpath + '/roomList.csv'):
            with open(fpath + '/roomList.csv','r',encoding='UTF-8') as file:
                checkData = []
                for i in csv.reader(file):
                    checkData.append(i)
                    count += 1
                    if(count == 2):
                        break
            checkDate = "".join(checkData[0])
            checkLocal = "".join(checkData[1])

            if(int(checkDate) != int(date) or int(checkLocal) != int(locate)):
                self.getApi(date,locate)
        else:
            self.getApi(date,locate)



    def roomList(self,date=nowDate,locate=sejong):
        self.checkFile(date,locate)
        count = 0
        try:
            with open(fpath + '/roomList.csv','r',encoding='UTF-8') as file:
                roomList = []
                for i in csv.reader(file):
                    count += 1
                    if count > 2:
                        roomList.append(i)
                return roomList
        except Exception as error:
            print("파일 처리 에러 발생",error)
        

    # def __del__(self):

    #     if os.path.isfile(fpath + '/roomList.csv'):
    #         os.remove(fpath + '/roomList.csv')


if __name__ == '__main__':
    test = getData()
    roomList = test.roomList('202205')
    print(roomList)
