import unittest
import sys
import os
import random
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from roominpy import search
#[Function] search.py 테스트 파일
#[DESC] search.py의 각 중요한 메소드 테스트
#[TODO] 테스트 목록 작성 및 코드 작성

'''
테스트 목록

1. 정렬이 제대로 동작하는지

2. 범위 검색 테스트 하기

3. 단어 검색 테스트 하기

5. 시간 평균 구하기

'''


class searchTest(unittest.TestCase):
    def setUp(self):
        self.search = search.search('202203','36110')
        self.wordList = ['0','0','0']

    def test_merge(self):
        m = search.merge()
        testList = [[random.randint(0,100) for col in range(10)] for row in range(10)]
        
        mergeList = m.mergeSort(testList,3)
        
        for i in mergeList:
            self.assertLessEqual(mergeList[0][3], i[3])
    
    def test_rangeSearch(self):
        testList, time = self.search.rangeSearch(7, 2004, 1977, self.wordList)
        self.assertNotEqual(len(testList), 0)
        self.assertIsInstance(time,float)


    def test_matchSearch(self):
        
        testList, time = self.search.matchSearch(7, '2004', self.wordList)
        self.assertNotEqual(len(testList), 0)
        self.assertIsInstance(time,float)

    def test_time(self):
        rangeTimeList = []
        matchTimeList = []
        for i in range(0,500,1):
            testList, rangeTime = self.search.rangeSearch(7,2004,1977,self.wordList)
            rangeTimeList.append(rangeTime)
            testList, matchTime = self.search.matchSearch(7,'2004',self.wordList)
            matchTimeList.append(matchTime)

        rangeLen = len(rangeTimeList)
        matchLen = len(matchTimeList)
        rangeTimeList.sort()
        matchTimeList.sort()
        print("")
        print("----------------------------------------------------------------------")
        print("최솟값")
        print("")
        print("범위 탐색")
        print(str(rangeTimeList[0]) + " 초")
        print("")
        print("매칭 탐색")
        print(str(matchTimeList[0]) + " 초")
        print("----------------------------------------------------------------------")
        print("평균값")
        print("")
        print("범위 탐색")
        print(str(sum(rangeTimeList,0.0)/rangeLen)  + " 초")
        print("")
        print("매칭 탐색")
        print(str(sum(matchTimeList,0.0)/matchLen)  + " 초")
        print("----------------------------------------------------------------------")
        print("최댓값")
        print("")
        print("범위 탐색")
        print(str(rangeTimeList[rangeLen-1])  + " 초")
        print("")
        print("매칭 탐색")
        print(str(matchTimeList[matchLen-1])  + " 초") 

if __name__ == '__main__':
    unittest.main()