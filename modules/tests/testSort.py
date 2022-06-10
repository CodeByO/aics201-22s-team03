import unittest
import sys
import os
import random
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from roominpy import sort
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

class sortTest(unittest.TestCase):
    def setUp(self):
        date = ['202112','202201','202202','202203','202204','202205']
        locate = ['36110','11110']
        self.s = sort.sort(date,locate)
        self.t = sort.ThreeSort()
    def test_merge(self):
        sorted = [[1,2,3,4,5,6],[1,3,4,5,6,7],[1,4,5,6,7,8],[1,5,6,7,8,9],[1,9,10,11,12,13],[1,8,9,10,11,12]]
        test = [[1,3,4,5,6,7],[1,2,3,4,5,6],[1,7,8,9,10,11],[1,5,6,7,8,9],[1,8,9,10,11,12],[1,9,10,11,12,13]]
        mSorted = self.t.mergeSort(test,2)
        self.assertEqual(mSorted[0],sorted[0])
    def test_insert(self):
        sorted = [[1,2,3,4,5,6],[1,3,4,5,6,7],[1,4,5,6,7,8],[1,5,6,7,8,9],[1,9,10,11,12,13],[1,8,9,10,11,12]]
        test = [[1,3,4,5,6,7],[1,2,3,4,5,6],[1,5,6,7,8,9],[1,7,8,9,10,11],[1,8,9,10,11,12],[1,9,10,11,12,13]]
        iSorted = self.t.insertSort(test,2)
        self.assertEqual(iSorted[0],sorted[0])
    def test_quick(self):
        sorted = [[1,2,3,4,5,6],[1,3,4,5,6,7],[1,4,5,6,7,8],[1,5,6,7,8,9],[1,9,10,11,12,13],[1,8,9,10,11,12]]
        test = [[1,3,4,5,6,7],[1,2,3,4,5,6],[1,5,6,7,8,9],[1,7,8,9,10,11],[1,8,9,10,11,12],[1,9,10,11,12,13]]
        qSorted = self.t.quickSort(test,2)
        self.assertEqual(qSorted[0],sorted[0])
    # def test_time(self):
    #     monthlyTimeList = []
    #     charterTimeList = []
    #     for i in range(0,50,1):
    #         monthly,charter,monthlyTime = self.suggest.suggestMonthly()
    #         monthlyTimeList.append(monthlyTime)
    #         charter, charterTime = self.suggest.suggestCharter()
    #         charterTimeList.append(charterTime)
        
    #     monthlyLen = len(monthlyTimeList)
    #     charterLen = len(charterTimeList)
    #     monthlyTimeList.sort()
    #     charterTimeList.sort()

    #     print("")
    #     print("----------------------------------------------------------------------")
    #     print("최솟값")
    #     print("")
    #     print("범위 탐색")
    #     print(str(monthlyTimeList[0]) + " 초")
    #     print("")
    #     print("매칭 탐색")
    #     print(str(charterTimeList[0]) + " 초")
    #     print("----------------------------------------------------------------------")
    #     print("평균값")
    #     print("")
    #     print("범위 탐색")
    #     print(str(sum(monthlyTimeList,0.0)/monthlyLen)  + " 초")
    #     print("")
    #     print("매칭 탐색")
    #     print(str(sum(charterTimeList,0.0)/charterLen)  + " 초")
    #     print("----------------------------------------------------------------------")
    #     print("최댓값")
    #     print("")
    #     print("범위 탐색")
    #     print(str(monthlyTimeList[monthlyLen-1])  + " 초")
    #     print("")
    #     print("매칭 탐색")
    #     print(str(charterTimeList[charterLen-1])  + " 초")    



if __name__ == '__main__':
    unittest.main()
