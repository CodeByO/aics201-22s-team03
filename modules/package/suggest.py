import queue
from getData import getData
import time



#[Function] 자료구조를 이용한 추천 기능
#[DESC] 힙을 이용하여 월세 또는 전세의 최저값인 데이터 리턴
#[TODO] python에 맞거나 더욱 효율적으로 로직 수정

class heap:

    def __init__(self):
        self.input = 0
        self.endPoint = 0
        self.heap = [[0]*5 for _ in range(10001)]
        

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
        
        while root * 2 + 1 < 10001 and value > self.heap[root*2] or value > self.heap[root* 2 + 1]:
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

        for i in self.heap:
            if i[index] != 0:
                return i         

class MinHeap:
    
    def __init__(self):
        self.heap = [0]
        self.current_size = 0
 
    def swim(self, i, index):
        while i // 2 > 0:
            if self.heap[i][index] < self.heap[i // 2][index]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2
 
    def insert(self, k, index):
        self.heap = k
        self.current_size += 1
        self.swim(self.current_size, index)

    def min_child(self, i, index):
        if (i * 2)+1 > self.current_size:
            return i * 2
        else:
            if self.heap[i*2][index] < self.heap[(i*2)+1][index]:
                return i * 2
            else:
                return (i * 2) + 1        
        
    def sink(self, i, index):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i, index)
            if self.heap[i][index] > self.heap[mc][index]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc
 
    def delete_min(self,index):
        if len(self.heap) == 1:
            return None

        root = self.heap[1]
        self.heap[1] = self.heap[self.current_size]
        *self.heap, _ = self.heap
        self.current_size -= 1
        self.sink(1,index)
        return root



class suggest:
    def __init__(self):
        data = getData.getData()
        self.monthly, self.charter = data.devideRoom('202203')

    def suggestMonthly(self):
        start = time.time()
        monthlyHeap = heap()
        charterHeap = heap()
        monthly = monthlyHeap.minHeap(self.monthly,3)
        charter = charterHeap.minHeap(self.monthly,4)
        end = time.time() - start
        return monthly, charter, round(end, 3)

    def suggestCharter(self):
        start = time.time()
        minHeap = heap()
        charter = minHeap.minHeap(self.charter,4)
        end = time.time() - start
        return charter, round(end, 3)

if __name__ == '__main__':
    data = getData()
    monthly, charter = data.devideRoom('202203')
    minheap = MinHeap()
    monthlyHeap = heap()
    monthlySort = monthlyHeap.minHeap(monthly,3)
    print(monthlySort)
    minheap.insert(monthly,3)
    print(minheap.heap[1])