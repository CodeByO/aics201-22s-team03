from roominpy.getData import getData
#from getData import getData
from datetime import datetime
import time
import traceback


#[Function] 자료구조를 이용한 추천 기능
#[DESC] 힙을 이용하여 월세 또는 전세의 최저값인 데이터 리턴



nowDate = datetime.today().strftime("%Y%m")
sejong = '36110'


class heap:

    def __init__(self):
        self.input = 0
        self.endPoint = 0
        self.heap = [[0]*7 for _ in range(100001)]
        

    def insertHeap(self, input,index):
        self.endPoint += 1

        cur = self.endPoint

        while cur > 0:

            if int(self.heap[cur // 2][index]) > int(input[index]):

                self.heap[cur] = self.heap[cur // 2]
                cur = cur // 2
            else:
                break
        self.heap.insert(cur,input)
        
    def popHeap(self,index):

        if self.endPoint == 0:
            return None
        root = 1
        value = self.heap[self.endPoint]

        self.heap[self.endPoint] = 0
        self.endPoint -= 1

        if self.endPoint == 0:
            return None
        while root * 2 + 1 < 10001 and int(value[index]) > int(self.heap[root*2][index]) or int(value[index]) > int(self.heap[root* 2 + 1][index]):
            if self.heap[root * 2][index] > self.heap[root * 2 + 1][index]:
                self.heap[root] = self.heap[root * 2 + 1]
                root = root * 2 + 1
            else:
                self.heap[root] = self.heap[root*2]
                root = root * 2        

        self.heap[root] = value

    def minHeap(self,list,index):
        for n in list:
            if(n[index] == '0'):
                self.popHeap(index)
            else:
                self.insertHeap(n,index)

        return self.heap[1]

class suggest:
    def __init__(self,date=nowDate,locate=sejong):
        data = getData()
        self.monthly, self.charter = data.devideRoom(date,locate)

    def suggestMonthly(self):
        start = time.perf_counter()
        monthlyHeap = heap()
        monthly = monthlyHeap.minHeap(self.monthly,5)
        charterHeap = heap()
        charter = charterHeap.minHeap(self.monthly,6)
        end = time.perf_counter() - start
        return monthly, charter, round(end, 3)

    def suggestCharter(self):
        start = time.perf_counter()
        minHeap = heap()
        charter = minHeap.minHeap(self.charter,6)
        end = time.perf_counter() - start
        return charter, round(end, 3)
