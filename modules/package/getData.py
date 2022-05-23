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
#[TODO] 여러 날짜 및 지역을 저장하는 코드 작성


class getData:
    
    def __init__(self):
        api_key = os.getenv('API_KEY')
        self.api_key = requests.utils.unquote(api_key)
        self.detchUrl = os.getenv('DETCH_URI')
        self.rowUrl = os.getenv('ROW_URI')
        self.mode = 1
    
    def getApi(self, date=nowDate,locate=sejong, mode=1):
        self.mode = mode
        params = {'serviceKey': self.api_key, 'LAWD_CD' : locate,'DEAL_YMD':date}
        detchResponse = None
        rowResponse = None
        try:
            detchResponse = requests.get(self.detchUrl,params=params).content
            rowResponse = requests.get(self.rowUrl,params=params).content
        except requests.exceptions.Timeout:
            print("[-]타임아웃 에러")
            return None
        except requests.exceptions.ConnectionError:
            print("[-]연결 에러")
            return None
    
        
        detchXmlData = xmltodict.parse(detchResponse)
        rowXmlData = xmltodict.parse(rowResponse)

        detchHeader = detchXmlData['response']['header']
        rowHeader = rowXmlData['response']['header']

        detchResultCode = detchHeader['resultCode']
        rowResultCode = rowHeader['resultCode']

        detchItems = None
        rowItems = None
        try:
            detchItems = detchXmlData['response']['body']['items']
            rowItems = rowXmlData['response']['body']['items']

        except:
            return None
        if detchResultCode != '00':
            resultMsg = detchHeader['resultMsg']
            print("[-]API 요청 에러 발생 resultCode : " + detchResultCode)
            print("------------------------------------")
            print("[-]"+resultMsg)
            print("------------------------------------")
            return None 
        elif rowResultCode != '00':
            resultMsg = rowHeader['resultMsg']
            print("[-]API 요청 에러 발생 resultCode : " + rowResultCode)
            print("------------------------------------")
            print("[-]"+resultMsg)
            print("------------------------------------")
            return None 


        if detchItems == None:
            print("[-]단독/다가구 API 요청 에러 발생")
            print("------------------------------------")
            print("[-]해당 하는 데이터가 없음")
            print("------------------------------------")
            return None
        elif rowItems == None:
            print("[-]연립주택 API 요청 에러 발생")
            print("------------------------------------")
            print("[-]해당 하는 데이터가 없음")
            print("------------------------------------")
            return None


        detchHouse = detchItems['item']
        rowHouse = rowItems['item']
        self.dictToList(detchHouse,rowHouse,date,locate)
        
    def dictToList(self,detch,row,date,locate):
        
        if detch == None:
            return None
        

        data = []
        #단독/다가구 데이터 일때 리스트 화
        for i in range(len(detch)):
            tmp = []
            tmp.append(self.findLocal(detch[i]['지역코드']))
            tmp.append(detch[i]['법정동'])
            tmp.append("단독/다가구")
            tmp.append(detch[i]['계약면적'])
            tmp.append(detch[i].get('층','0'))
            tmp.append(detch[i]['월세금액'])
            tmp.append(detch[i]['보증금액'].replace(",",""))
            tmp.append(detch[i].get('건축년도','0000'))
            data.append(tmp)

        for i in range(len(row)):
            tmp = []
            tmp.append(self.findLocal(row[i]['지역코드']))
            tmp.append(row[i]['법정동'])
            tmp.append(row[i]['연립다세대'])
            tmp.append(row[i]['전용면적'])
            tmp.append(row[i].get('층','0'))
            tmp.append(row[i]['월세금액'])
            tmp.append(row[i]['보증금액'].replace(",",""))
            tmp.append(row[i].get('건축년도','0000'))
            data.append(tmp)

        if self.mode == 1:
            # 일반적인 데이터 요청을 파일로 저장
            with open(fpath + '/roomList.csv', 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(date)
                writer.writerow(locate)
                writer.writerows(data)
                file.close()
        elif self.mode == 2:
            # 지역을 리스트로 받을 때 받은 요청을 파일로 저장
            with open(fpath + '/roomList.csv', 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(date)
                writer.writerow(locate)
                writer.writerows(data)
                file.close()

        elif self.mode == 3:
            # 날짜를 리스트로 받을 때 받은 요청을 파일로 저장
            with open(fpath + '/roomList.csv', 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(date)
                writer.writerow(locate)
                writer.writerows(data)
                file.close()

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
                file.close()
            return monthly, charter
        except Exception as error:
            print("[-]파일 처리 에러 발생",error)
            return None
    
    def checkFile(self,date=nowDate,locate=sejong):
        count = 0

        if os.path.isfile(fpath + '/roomList.csv'):
            with open(fpath + '/roomList.csv','r',encoding='UTF-8') as file:
                checkData = []
                for i in csv.reader(file):
                    checkData.append(i)
                    count += 1
                    if count == 2:
                        break
            checkDate = "".join(checkData[0])
            checkLocal = "".join(checkData[1])
            file.close()

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
                file.close()
                return roomList
                
        except Exception as error:
            print("[-]파일 처리 에러 발생",error)
            return None
        
    def locateList(self,locate,date=nowDate):
        locateMode = 2
        if locate is list:
            for i in locate:
                self.getApi(date,i,locateMode)

            try:
                with open(fpath + '/locateList.csv','r',encoding='UTF-8') as file:
                    roomList = []
                    for i in csv.reader(file):
                        count += 1
                        if count > 2:
                            roomList.append(i)
                    file.close()
                    return roomList
                
            except Exception as error:
                print("[-]파일 처리 에러 발생",error)
                return None

        else:
            return None 
                   

    def dateList(self,date,locate=sejong):
        dateMode = 3
        if date is list:
            for i in date:
                self.getApi(i,locate,dateMode)
            
            try:
                with open(fpath + '/dateList.csv','r',encoding='UTF-8') as file:
                    roomList = []
                    for i in csv.reader(file):
                        count += 1
                        if count > 2:
                            roomList.append(i)
                    file.close()
                    return roomList
                
            except Exception as error:
                print("[-]파일 처리 에러 발생",error)
                return None

        else:
            return None
    # def __del__(self):

    #     if os.path.isfile(fpath + '/roomList.csv'):
    #         os.remove(fpath + '/roomList.csv')


if __name__ == '__main__':
    test = getData()
    roomList = test.roomList('202105','36110')
    print(roomList[0])