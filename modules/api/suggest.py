from calendar import month
from getData import getData




#[Function] 자료구조를 이용한 추천 기능
#[DESC] 힙을 이용하여 월세 또는 전세의 최저값인 데이터 리턴
#[TODO] 기능 작성




class suggestRoom:
    def __init__(self):
        data = getData()
        self.monthly, self.charter = data.devideRoom('202203')

    
