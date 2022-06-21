import unittest
import sys
import os
from datetime import datetime
import csv
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from getData import getData
#[Function] getData.py 테스트 파일
#[DESC] getData.py의 각 중요한 메소드 테스트


'''
테스트 목록

1. roomList 파일이 제대로 생성이 되었는지

2. 리스트 변환이 잘 이루어져 있는지(리스트 반환값이 존재 하는지)

3. 리스트 안에 데이터가 맞게 들어갔는지

4. 다른 인자로 요청시 파일이 맞게 변경되어 저장되는지

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
       self.assertTrue(os.path.isfile('../data/roomList.csv'))
       self.assertTrue(os.path.isfile('../data/roomList.csv.check'))
    
    def test_locateListFile(self):
        date = datetime.today().strftime("%Y%m")
        locate = ['36110','11110']
        roomList = self.data.roomList(date,locate)
        self.assertTrue(os.path.isfile('../data/locateList.csv'))
        self.assertTrue(os.path.isfile('../data/locateList.csv.check'))

    def test_dateListFile(self):
        date = ['202201','202202']
        locate = '36110'
        roomList = self.data.roomList(date,locate)
        self.assertTrue(os.path.isfile('../data/dateList.csv'))
        self.assertTrue(os.path.isfile('../data/dateList.csv.check'))
    
    def test_dateListFile(self):
        date = ['202201','202202']
        locate = ['36110','11110']
        roomList = self.data.roomList(date,locate)
        self.assertTrue(os.path.isfile('../data/multiList.csv'))
        self.assertTrue(os.path.isfile('../data/multiList.csv.check'))

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
        if os.path.isfile('../data/roomList.csv') and os.path.isfile('../data/roomList.csv.check'):
            with open("../data/roomList.csv.check","r",encoding='utf-8', newline='') as file:
                for i in csv.reader(file):
                    beforData.append(i)
        afterData = []

        self.data.getApi(date,locate)
        if os.path.isfile('../data/roomList.csv') and os.path.isfile('../data/roomList.csv.check'):
            with open("../data/roomList.csv.check","r",encoding='utf-8', newline='') as file:
                for i in csv.reader(file):
                    afterData.append(i)

        self.assertNotEqual(beforData,afterData)


    def testDown(self):
        if os.path.isfile('../data' + '/roomList.csv'):
            os.remove('../data' + '/roomList.csv')
            os.remove('../data' + '/roomList.csv.check')
        if os.path.isfile('../data' + '/dateList.csv'):
            os.remove('../data' + '/dateList.csv')
            os.remove('../data' + '/dateList.csv.check')

        if os.path.isfile('../data' + '/locateList.csv'):
            os.remove('../data' + '/locateList.csv')
            os.remove('../data/' + '/locateList.csv.check')
        if os.path.isfile('../data' + '/multiList.csv'):
            os.remove('../data' + '/multiList.csv')
            os.remove('../data' + '/multiList.csv.check')


if __name__ == '__main__':
    unittest.main()