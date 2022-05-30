import unittest
import sys
import os
from datetime import datetime
import csv
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from package.getData import getData
import asyncio
#[Function] getData.py 테스트 파일
#[DESC] getData.py의 각 중요한 메소드 테스트
#[TODO] test_checkFile 메서드 완성 및 에러 테스트 완성
#[ISSUE] test_checkFile에서 getAPI 메서드 호출 시 데이터를 받아오지 못함

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
            self.assertEqual(len(i),8)

    def test_devideRoom(self):
        for i in self.monthly:
            self.assertEqual(len(i),8)
        for i in self.charter:
            self.assertEqual(len(i), 8)
    
    def test_getApiError(self):
        pass

    # def test_checkFile(self):
    #     date = '202204'
    #     locate = '11110'
    #     roomList = self.data.roomList(date, locate)
    #     print(roomList[0])


    def test_checkFile(self):
        date = '202104'
        locate = '11110'

        roomList = self.data.roomList(date,locate)

        self.assertEqual(self.roomList[0],roomList[0]) 


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