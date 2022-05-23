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
#[ISSUE] locateList와 dateList 메서드 실행시 어떤 방식으로 여러개 데이터를 요청해서 저장할지 고민 중 

class getData:
    
    def __init__(self):
        api_key = os.getenv('API_KEY')
        self.api_key = requests.utils.unquote(api_key)
        self.detchUrl = os.getenv('DETCH_URI')
        self.rowUrl = os.getenv('ROW_URI')
        self.mode = 1
        self.fileName = '/roomList.csv'


    def getApi(self, date=nowDate,locate=sejong,mode=1):
        if type(locate) is list:
            self.fileName = '/locateList.csv'
            self.mode = 2
        elif type(date) is list:
            self.fileName = '/dateList.csv'
            self.mode = 3
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
 

        item = detchItems['item'] + rowItems['item']
        self.dictToList(item,date,locate)
        
    def dictToList(self,item,date,locate):
        print(self.fileName)
        if item == None:
            return None
        data = []
        for i in range(len(item)):
            
            tmp = []
            tmp.append(self.findLocal(item[i]['지역코드']))
            tmp.append(item[i]['법정동'])
            tmp.append(item[i]['연립다세대'] if item[i].__contains__('연립다세대') else "단독/다가구")
            tmp.append(item[i]['계약면적'] if item[i].__contains__('계약면적') else item[i]['전용면적'])
            tmp.append(item[i].get('층','0'))
            tmp.append(item[i]['월세금액'])
            tmp.append(item[i]['보증금액'].replace(",",""))
            tmp.append(item[i].get('건축년도','0000'))
            data.append(tmp)

        if self.mode == 1:
            with open(fpath + self.fileName, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(date)
                writer.writerow(locate)
                writer.writerows(data)
                file.close()
                # 일반적인 데이터 요청을 파일로 저장
        elif self.mode == 2:
            # 지역을 리스트로 받을 때 받은 요청을 파일로 저장
            with open(fpath + self.fileName, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(date)
                writer.writerow(locate)
                writer.writerows(data)
                file.close()

        elif self.mode == 3:
            # 날짜를 리스트로 받을 때 받은 요청을 파일로 저장
            # with open(fpath + '/dateList.csv', 'w', encoding='utf-8', newline='') as file:
            #     writer = csv.writer(file)
            #     writer.writerow(date)
            #     writer.writerow(locate)
            #     writer.writerows(data)
            #     file.close()
            if os.path.isfile(fpath + self.fileName):
                with open(fpath + self.fileName, 'w', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
                    file.close()
            else:
                with open(fpath + self.fileName, 'w', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(date)
                    writer.writerow(locate)
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
            with open(fpath + self.fileName,'r',encoding='UTF-8') as file:
                
                roomList = csv.reader(file)
                monthly = []
                
                charter = []

                for i in roomList:
                    count += 1
                    if count < 3:
                        continue
                    if i[4] == '0':
                        charter.append(i)
                    else:
                        monthly.append(i)    
                file.close()
            return monthly, charter
        except Exception as error:
            print("[-]파일 처리 에러 발생",error)
            return None
    
    def checkFile(self,date=nowDate,locate=sejong):
        print(self.fileName)
        count = 0

        if os.path.isfile(fpath + self.fileName):
            with open(fpath + self.fileName,'r',encoding='UTF-8') as file:
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
                os.remove(fpath + self.fileName)
                self.getApi(date,locate)
        else:
            self.getApi(date,locate)



    def roomList(self,date=nowDate,locate=sejong):
        # self.checkFile(date,locate)
        count = 0
        try:
            with open(fpath + '/roomList.csv','r',encoding='UTF-8') as file:
                roomList = []
                for i in csv.reader(file):
                    count += 1
                    if count < 3:
                        continue
                    roomList.append(i)
                file.close()
                return roomList
                
        except Exception as error:
            print("[-] roomList.csv 파일 처리 에러 발생",error)
            return None
        
    def locateList(self,date,locate):
        if date == None or locate == None :
            return None
        locateMode = 2
        print(type(locate))
        if type(locate) is list:
            print("list 조건 통과")
            self.getApi(date,locate)
            count = 0
            try:
                with open(fpath + self.fileName,'r',encoding='UTF-8') as file:
                    roomList = []
                    for i in csv.reader(file):
                        count += 1
                        if count < 3:
                            continue
                        roomList.append(i)
                    file.close()
                    return roomList
                
            except Exception as error:
                print("[-] locateList.csv 파일 처리 에러 발생")
                return None

        else:
            return None 
                   

    def dateList(self,date,locate=sejong):
        
        if date == None or locate == None :
            return None

        dateMode = 3
        if type(date) is list:
            self.getApi(date,locate)
            count = 0
            try:
                with open(fpath + self.fileName,'r',encoding='UTF-8') as file:
                    roomList = []
                    for i in csv.reader(file):
                        count += 1
                        if count < 3:
                            continue
                        roomList.append(i)
                    file.close()
                    return roomList
                
            except Exception as error:
                print("[-] dateList.csv 파일 처리 에러 발생",error)
                return None

        else:
            return None
    # def __del__(self):

    #     if os.path.isfile(fpath + '/roomList.csv'):
    #         os.remove(fpath + '/roomList.csv')
    #     if os.path.isfile(fpath + '/dateList.csv'):
    #         os.remove(fpath + '/dateList.csv')
    #     if os.path.isfile(fpath + '/locateList.csv'):
    #         os.remove(fpath + '/locateList.csv')


if __name__ == '__main__':
    test = getData()
    date = ['202201','202202','202203','202204','202205']
    locate = ['36110','11110']
    roomList = test.dateList(date,'36110')