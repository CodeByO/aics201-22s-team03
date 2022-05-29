import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from suggest import *

#[Function] suggest.py 테스트 파일
#[DESC] suggest.py의 중요한 메서드 테스트
#[TODO] 자료형 이외에 테스트 할것이 있는지 고민 핑요
'''
테스트 목록

1. 간단한 2차원 리스트를 heap 클래스에 넣었을 때 최솟값이 제대로 출력되는지

2. 월세 추천의 반환 값이 맞는 데이터가 나오는지

3. 전세 추천의 반환 값이 맞는 데이터가 나오는지 

4. 여러번 정렬 후 최고 시간, 최저 시간, 평균 시간 구하기
'''

class suggestTest(unittest.TestCase):
    def setUp(self):
        self.heap = heap()
        self.suggest = suggest()

    def test_heap(self):

        test = [
            [0,0,10,0],[0,0,9,0],
            [0,0,8,0],[0,0,7,0],
            [0,0,1,0],[0,0,5,0],
            [0,0,4,0],[0,0,3,0],
            [0,0,2,0],[0,0,6,0]
        ]
        min = self.heap.minHeap(test,2)
        self.assertListEqual(min,test[4])

    def test_monthlySuggest(self):
        monthly,charter,time = self.suggest.suggestMonthly()
        self.assertIsInstance(monthly, list)
        self.assertIsInstance(charter, list)
        self.assertIsInstance(time, float)

    def test_charterSuggest(self):
        charter,time = self.suggest.suggestCharter()
        self.assertIsInstance(charter, list)
        self.assertIsInstance(time, float)


if __name__ == '__main__':
    unittest.main()
