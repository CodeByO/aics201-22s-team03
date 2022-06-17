import requests
import os
from dotenv import load_dotenv
import xmltodict
import csv
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

nowDate = datetime.today().strftime("%Y%m")
sejong = '36110'
load_dotenv(verbose=True)
fpath = os.path.dirname(os.path.abspath(__file__))

#[Function] Open API 데이터 호출
#[DESC] 지역코드와 날짜를 인자로 받아 Open API의 데이터 조회 후 리스트 화 하여 파일로 저장

class getData:
    
    def __init__(self):
        api_key = os.getenv('API_KEY')
        self.api_key = requests.utils.unquote(api_key)
        self.detchUrl = os.getenv('DETCH_URI')
        self.rowUrl = os.getenv('ROW_URI')
        self.fileName = '/roomList.csv'

    def getUrl(self,url):
        try:
            return requests.get(url[0],params=url[1]).content
        except requests.exceptions.Timeout:
            print("[-]타임아웃 에러")
            return None
        except requests.exceptions.ConnectionError:
            print("[-]연결 에러")
            return None
        except requests.exceptions:
            print("[-]요청 에러")
            return None

    def getApi(self, date=nowDate,locate=sejong):

        if type(locate) is list and type(date) is str:
            dateRequestList = []
            self.fileName = '/locateList.csv'
            for i in locate:
                params = {'serviceKey': self.api_key, 'LAWD_CD' : i,'DEAL_YMD':date}
                dateRequestList.append([self.detchUrl,params])
                dateRequestList.append([self.rowUrl,params])

        elif type(locate) is str and type(date) is list:
            self.fileName = '/dateList.csv'
            dateRequestList = []
            for i in date:
                params = {'serviceKey': self.api_key, 'LAWD_CD' : locate,'DEAL_YMD':i}
                dateRequestList.append([self.detchUrl,params])          
                dateRequestList.append([self.rowUrl,params])

        elif type(date) is list and type(date) is list:
            dateRequestList = []
            self.fileName = '/multiList.csv'
            for i in locate:
                for j in date:
                    params = {'serviceKey': self.api_key, 'LAWD_CD' : i,'DEAL_YMD':j}
                    dateRequestList.append([self.detchUrl,params])
                    dateRequestList.append([self.rowUrl,params])
        
        else:
            self.fileName = '/roomList.csv'
            dateRequestList = []
            params = {'serviceKey': self.api_key, 'LAWD_CD' : locate,'DEAL_YMD':date}
            dateRequestList.append([self.detchUrl,params])
            dateRequestList.append([self.rowUrl,params])

        responseList = []
        with ThreadPoolExecutor(max_workers=10) as pool:
            responseList = list(pool.map(self.getUrl,dateRequestList))
        
        item = []
        for i in responseList:
            check = self.checkData(i)
            if check == None:
                return None
            else:
                item += check
        
        self.dictToList(item,date,locate)
    
    def checkData(self,data):
        if data == None:
            return None
        xmlData = xmltodict.parse(data)

        header = xmlData['response']['header']

        resultCode = header['resultCode']

        items = None
        try:
            items = xmlData['response']['body']['items']['item']

        except:

            if items == None:
                print("[-]API 요청 에러 발생")
                print("------------------------------------")
                print("[-]해당 하는 데이터가 없음")
                print("------------------------------------")
                return None
                
        
        if resultCode != '00':
            resultMsg = header['resultMsg']
            print("[-]API 요청 에러 발생 resultCode : " + resultCode)
            print("------------------------------------")
            print("[-]"+resultMsg)
            print("------------------------------------")
            return None
        return items

    def dictToList(self,item,date,locate):
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
            tmp.append(item[i]['월세금액'].replace(",",""))
            tmp.append(item[i]['보증금액'].replace(",",""))
            tmp.append(item[i].get('건축년도','0000'))
            data.append(tmp)

        if os.path.isfile(fpath+self.fileName):
            with open(fpath + self.fileName, 'a', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
                file.close()
        else:
            with open(fpath + self.fileName, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
                file.close()
        with open(fpath + self.fileName + ".check","w",encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(date)
                writer.writerow(locate)
                file.close

    def findLocal(self,target):
        with open(fpath + '/regionCode.csv','r',encoding='UTF-8') as file:
    
            reader = csv.reader(file)
            match = [s for s in reader if target in s] 
            if match == []:
                return None
                
        return match[0][0]

    def roomList(self,date=nowDate,locate=sejong):
        self.checkFile(date,locate)
        try:
            with open(fpath + self.fileName,'r',encoding='UTF-8') as file:
                roomList = []
                for i in csv.reader(file):
                    roomList.append(i)
                file.close()
                return roomList
                
        except Exception as error:
            print("[-]" + self.fileName + " 파일 처리 에러 발생",error)
            return None


    def devideRoom(self,date=nowDate,locate=sejong):
        self.checkFile(date,locate)
        try:
            with open(fpath + self.fileName,'r',encoding='UTF-8') as file:
                
                roomList = csv.reader(file)
                monthly = []
                
                charter = []

                for i in roomList:
                    if i[5] == '0':
                        charter.append(i)
                    else:
                        if i[6] != '0':
                            monthly.append(i)    
                file.close()
            return monthly, charter
        except Exception as error:
            print("[-]파일 처리 에러 발생",error)
            return None
    
    def checkFile(self,date=nowDate,locate=sejong):
        if type(locate) is list and type(date) is str:
            self.fileName = '/locateList.csv'

        elif type(locate) is str and type(date) is list:
            self.fileName = '/dateList.csv'

        elif type(date) is list and type(date) is list:

            self.fileName = '/multiList.csv'
        
        else:
            self.fileName = '/roomList.csv'

        checkDate = ""
        checkLocal = ""
        checkData = []
    
        if os.path.isfile(fpath + self.fileName) and os.path.isfile(fpath + self.fileName + ".check"):
            with open(fpath + self.fileName + ".check","r",encoding='utf-8', newline='') as file:
                for i in csv.reader(file):
                    checkData.append(i)
            checkDate = "".join(checkData[0])
            checkLocal = "".join(checkData[1])
            file.close()
        dateStr = ''.join(map(str, date))
        locateStr = ''.join(map(str, locate))
        if(checkDate != dateStr or checkLocal != locateStr):
            self.getApi(date,locate)
        else:
            return None



    # def __del__(self):

    #     if os.path.isfile(fpath + '/roomList.csv'):
    #         os.remove(fpath + '/roomList.csv')
    #         os.remove(fpath + '/roomList.csv.check')
    #     if os.path.isfile(fpath + '/dateList.csv'):
    #         os.remove(fpath + '/dateList.csv')
    #         os.remove(fpath + '/dateList.csv.check')

    #     if os.path.isfile(fpath + '/locateList.csv'):
    #         os.remove(fpath + '/locateList.csv')
    #         os.remove(fpath + '/locateList.csv.check')
    #     if os.path.isfile(fpath + '/multiList.csv'):
    #         os.remove(fpath + '/multiList.csv')
    #         os.remove(fpath + '/multiList.csv.check')
