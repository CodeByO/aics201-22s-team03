from package import getData
from datetime import datetime
import time
import copy


#[Function] 자료구조를 이용한 각 요소 정렬
#[DESC] 면적, 월세, 전세 각 분야를 3가지 정렬로 각각 정렬
#[TODO] 면적 정렬 추가 후 데이터와 수행 시간 측정은 어디서 넣어줄건지 고민

nowDate = datetime.today().strftime("%Y%m")
sejong = '36110'

class TreeSort:
    def insertSort(self,roomList,index):
        data = copy.deepcopy(roomList)
        for j in range(1, len(data)):
            for i in range(j, 0, -1):
                if data[i][index] < data[i-1][index]:
                    data[i], data[i-1] = data[i-1], data[i]
                else:
                    break
        return data

    def mergeSort(self, roomList, index):
        data = copy.deepcopy(roomList)
        if len(data) < 2:
            return data
        low = [[0]*5 for _ in range(500)]
        high = [[0]*5 for _ in range(500)]
        
            # 리스트 초기화
        

        middle = len(data) // 2 # data 길이 중간 값 취함    

        low = self.mergeSort(data[:middle], index)
        high = self.mergeSort(data[middle:], index)   

        merged = []
        h = l = 0

        while l < len(low) and h < len(high):
            if float(low[l][index]) < float(high[h][index]):
                merged.append(low[l])
                l += 1
            else:
                merged.append(high[h])
                h += 1

        merged += low[l:]
        merged += high[h:]

        return merged

    def quickSort(self, roomList, index, first, final):
        
        data = copy.deepcopy(roomList)
        
        if first >= final:
            return
        
        pivot = first
        low = first + 1
        high = final

        while low <= high:
            while low <= final and float(data[low][index]) <= float(data[pivot][index]):
                low +=1
            while high>first and float(data[high][index]) >= float(data[pivot][index]):
                high -= 1
            if low > high:
                data[high],data[pivot] = data[pivot],data[high]
            else:
                data[low],data[high]=data[pivot],data[low]
        
        self.quickSort(data, index, first, high-1)
        

        return data

class sort:

    def __init__(self,date=nowDate,locate=sejong):
        data = getData.getData()
        self.roomList = data.roomList(date,locate)
    def area(self,typeIndex):
        index = 3
        areaS = TreeSort()
        sorted = []
        if typeIndex == 1:
            start = time.perf_counter()
            sorted = areaS.insertSort(self.roomList, index)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif typeIndex == 2:
            start = time.perf_counter()
            sorted = areaS.mergeSort(self.roomList, index)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif typeIndex == 3:
            start = time.perf_counter()
            sorted = areaS.quickSort(self.roomList, index, 0, len(self.roomList)-1)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        else:
            return
    def charter(self, typeIndex):
        index = 6
        areaS = TreeSort()
        sorted = []
        if typeIndex == 1:
            start = time.perf_counter()
            sorted = areaS.insertSort(self.roomList, index)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif typeIndex == 2:
            start = time.perf_counter()
            sorted = areaS.mergeSort(self.roomList, index)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif typeIndex == 3:
            start = time.perf_counter()
            sorted = areaS.quickSort(self.roomList, index, 0, len(self.roomList)-1)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        else:
            return
    
    def monthly(self, typeIndex):
        index = 5
        areaS = TreeSort()
        sorted = []
        if typeIndex == 1:
            start = time.perf_counter()
            sorted = areaS.insertSort(self.roomList, index)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif typeIndex == 2:
            start = time.perf_counter()
            sorted = areaS.mergeSort(self.roomList, index)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif typeIndex == 3:
            start = time.perf_counter()
            sorted = areaS.quickSort(self.roomList, index, 0, len(self.roomList)-1)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        else:
            return


# if __name__ == '__main__':
#     s = sort()
#     data = getData.getData()
#     roomList = data.roomList()
#     newd=s.mergeSort(roomList, 2)
#     quickList =  s.quickSort(roomList, 0, len(roomList)-1)
#     insertList = s.insertSort(roomList, 2)

#     # print('----------------mergeSort-------------------')

#     # for i in newd:
#     #     print(i[2])
    
#     print('----------------quickSort-------------------')

#     for i in insertList:
#         print(i[2])

    