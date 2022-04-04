from asyncio.proactor_events import _ProactorBasePipeTransport
from calendar import month
from getData import getData




#[Function] 자료구조를 이용한 추천 기능
#[DESC] 힙을 이용하여 월세 또는 전세의 최저값인 데이터 리턴
#[TODO] 기능 작성




class suggest:
    def __init__(self):
        data = getData()
        self.monthly, self.charter = data.devideRoom('202203')
        self.N = 0
        self.input = 0
        self.endPoint = 0
        self.heap = [0 for i in range(100001)]
    
    def suggestMonthly(self):
        pass

    def suggestCharter(self):
        pass

    def insertHeap(self, input):
        self.endPoint += 1

        cur = self.endPoint

        while cur > 0:
            if self.heap[cur / 2] > input :
                self.heap.insert(cur,self.heap[cur/2])
                cur = cur / 2
            else:
                break
        self.heap.insert(cur,input)
        
    def popHeap(self):
        if self.endPoint == 0:
            print("0")
            return None
        root = 1
        returnValue = self.heap[root]
        value = self.heap[self.endPoint]
        self.heap.insert(self.endPoint,0)
        self.endPoint -= 1

        if self.endPoint == 0:
            print(returnValue)
            return None
        