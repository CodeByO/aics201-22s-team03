import unittest
import sys
import os
import random
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from package import sort
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
        pass



if __name__ == '__main__':
    unittest.main()
