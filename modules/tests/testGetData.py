import unittest
import sys
import os
from datetime import datetime
import csv
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from roominpy.getData import getData
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
def message():
    raise Exception("[-]API 요청 에러 발생")

class getDataTest(unittest.TestCase):


    def setUp(self):
        self.data = getData()
        local = '36110'
        nowDate = datetime.today().strftime("%Y%m")
        self.data.getApi(nowDate,local)
        self.roomList = self.data.roomList(nowDate,local)
        self.monthly,self.charter = self.data.devideRoom(nowDate,local)

    def test_roomListFile(self):
       self.assertTrue(os.path.isfile('../roominpy/roomList.csv'))
       self.assertTrue(os.path.isfile('../roominpy/roomList.csv.check'))
    
    def test_locateListFile(self):
        date = datetime.today().strftime("%Y%m")
        locate = ['36110','11110']
        roomList = self.data.roomList(date,locate)
        self.assertTrue(os.path.isfile('../roominpy/locateList.csv'))
        self.assertTrue(os.path.isfile('../roominpy/locateList.csv.check'))

    def test_dateListFile(self):
        date = ['202201','202202']
        locate = '36110'
        roomList = self.data.roomList(date,locate)
        self.assertTrue(os.path.isfile('../roominpy/dateList.csv'))
        self.assertTrue(os.path.isfile('../roominpy/dateList.csv.check'))
    
    def test_dateListFile(self):
        date = ['202201','202202']
        locate = ['36110','11110']
        roomList = self.data.roomList(date,locate)
        self.assertTrue(os.path.isfile('../roominpy/multiList.csv'))
        self.assertTrue(os.path.isfile('../roominpy/multiList.csv.check'))

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


    def test_checkFile(self):
        date = '202205'
        locate = '11110'
        beforData = []
        if os.path.isfile('../roominpy/roomList.csv') and os.path.isfile('../roominpy/roomList.csv.check'):
            with open("../roominpy/roomList.csv.check","r",encoding='utf-8', newline='') as file:
                for i in csv.reader(file):
                    beforData.append(i)
        afterData = []

        self.data.getApi(date,locate)
        if os.path.isfile('../roominpy/roomList.csv') and os.path.isfile('../roominpy/roomList.csv.check'):
            with open("../roominpy/roomList.csv.check","r",encoding='utf-8', newline='') as file:
                for i in csv.reader(file):
                    afterData.append(i)

        self.assertNotEqual(beforData,afterData)


    def testDown(self):
        if os.path.isfile('../roominpy' + '/roomList.csv'):
            os.remove('../roominpy' + '/roomList.csv')
            os.remove('../roominpy' + '/roomList.csv.check')
        if os.path.isfile('../roominpy' + '/dateList.csv'):
            os.remove('../roominpy' + '/dateList.csv')
            os.remove('../roominpy' + '/dateList.csv.check')

        if os.path.isfile('../roominpy' + '/locateList.csv'):
            os.remove('../roominpy' + '/locateList.csv')
            os.remove('../roominpy' + '/locateList.csv.check')
        if os.path.isfile('../roominpy' + '/multiList.csv'):
            os.remove('../roominpy' + '/multiList.csv')
            os.remove('../roominpy' + '/multiList.csv.check')


if __name__ == '__main__':
    unittest.main()