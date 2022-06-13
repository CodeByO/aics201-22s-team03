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

    def test_time(self):
        mergeTimeList = []
        insertTimeList = []
        quickTimeList = []

        for i in range(0,50,1):
            insertList, insertTime = self.s.area(1,0)
            mergeList, mergeTime = self.s.area(2,0)
            quickList, quickTime = self.s.area(3,0)

            insertTimeList.append(insertTime)
            mergeTimeList.append(mergeTime)
            quickTimeList.append(quickTime)
        
        insertTimeList.sort()
        mergeTimeList.sort()
        quickTimeList.sort()

        insertLen = len(insertTimeList)
        mergeLen = len(mergeTimeList)
        quickLen = len(quickTimeList)
        print("")
        print("----------------------------------------------------------------------")
        print("최솟값")
        print("")
        print("삽입 정렬")
        print(str(insertTimeList[0]) + " 초")
        print("")
        print("합병 정렬")
        print(str(mergeTimeList[0]) + " 초")
        print("")
        print("퀵 정렬")
        print(str(quickTimeList[0]) + " 초")
        print("----------------------------------------------------------------------")
        print("평균값")
        print("")
        print("삽입 정렬")
        print(str(round(sum(insertTimeList,0.0)/insertLen,3))  + " 초")
        print("")
        print("합병 정렬")
        print(str(round(sum(mergeTimeList,0.0)/mergeLen,3)) + " 초")
        print("")
        print("퀵 정렬")
        print(str(round(sum(quickTimeList,0.0)/quickLen,3))  + " 초")
        print("----------------------------------------------------------------------")
        print("최댓값")
        print("")
        print("삽입 정렬")
        print(str(insertTimeList[insertLen-1])  + " 초")
        print("")
        print("합병 정렬")
        print(str(mergeTimeList[mergeLen-1])  + " 초")
        print("")
        print("퀵 정렬")
        print(str(quickTimeList[quickLen-1])  + " 초") 

if __name__ == '__main__':
    unittest.main()
