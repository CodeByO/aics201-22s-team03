import unittest
import sys
import os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from getData import getData


'''
테스트 목록

1. roomList 파일이 제대로 생성이 되었는지

2. 리스트 변환이 잘 이루어져 있는지(리스트 반환값이 존재 하는지)

3. 리스트 안에 데이터가 맞게 들어갔는지

4. 기존에 작성한 에러 처리가 제대로 동작 하는지
'''


class getDataTest(unittest.TestCase):


    def setUp(self):
        self.data = getData()
        local = '36110'
        nowDate = datetime.today().strftime("%Y%m")
        self.data.getApi(nowDate,local)
        self.roomList = self.data.roomList(nowDate,local)
        self.monthly,self.charter = self.data.devideRoom(nowDate,local)
    

    def test_file(self):
       self.assertTrue(os.path.isfile('../roomList.csv'))
        

    def test_list(self):
        self.assertIsInstance(self.roomList, list)
        self.assertIsInstance(self.monthly, list)
        self.assertIsInstance(self.charter, list)

    def test_roomList(self):
        for i in self.roomList:
            self.assertEqual(len(i),6)

    def test_devideRoom(self):
        for i in self.monthly:
            self.assertEqual(len(i),6)
        for i in self.charter:
            self.assertEqual(len(i), 6)
    
    def test_getApiError(self):
        pass
    
    def test_checkFile(self):
        pass


    # def test_checkFile(self):
    #     date = '202203'
    #     locate = '31000'

    #     count = 0
    #     count2 = 0
    #     with open('../roomList.csv','r',encoding='UTF-8') as file:
    #         checkData = []
    #         for i in csv.reader(file):
    #             checkData.append(i)
    #             count += 1
    #             if(count == 2):
    #                 break
    #     checkDate = "".join(checkData[0])
    #     checkLocal = "".join(checkData[1])


    #     self.data.getApi(date,locate)

    #     with open('../roomList.csv','r',encoding='UTF-8') as file:
    #         checkData2 = []
    #         for i in csv.reader(file):
    #             checkData2.append(i)
    #             count2 += 1
    #             if(count2 == 2):
    #                 break
    #     checkDate2 = "".join(checkData[0])
    #     checkLocal2 = "".join(checkData[1])

    #     if self.assertNotEqual(checkDate,checkDate2) and self.assertNotEqual(checkLocal,checkLocal2):
    #         print("[+]checkFile 통과") 
    #         print("----------------------------------------------------------------------")
    #     else:
    #         print("[-]checkFile 실패") 
    #         print("----------------------------------------------------------------------")

    # def testDown(self):
    #     try:
    #         os.remove('../roomList.csv')
    #         print("[+] 테스트 후 파일 삭제 성공")
    #         print("----------------------------------------------------------------------")  
    #     except:
    #         print("[-]파일 삭제 실패")
    #         print("----------------------------------------------------------------------")     


if __name__ == '__main__':
    unittest.main()