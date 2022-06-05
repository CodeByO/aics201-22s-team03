from package import getData
from datetime import datetime
import time
import copy


#[Function] 자료구조를 이용한 각 요소 정렬
#[DESC] 면적, 월세, 전세 각 분야를 3가지 정렬로 각각 정렬
#[TODO] 면적 정렬 추가 후 데이터와 수행 시간 측정은 어디서 넣어줄건지 고민

nowDate = datetime.today().strftime("%Y%m")
sejong = '36110'

class ThreeSort:
    def insertSort(self,roomList,index):
        data = copy.deepcopy(roomList)
        for j in range(1, len(data)):
            for i in range(j, 0, -1):
                if float(data[i][index]) < float(data[i-1][index]):
                    data[i], data[i-1] = data[i-1], data[i]
                else:
                    break
        return data

    def mergeSort(self, roomList, index):
        list = copy.deepcopy(roomList)
        size = len(list)
        if size <= 1:
            return list
        mid = len(list) // 2
        left = self.mergeSort(list[:mid],index)
        right = self.mergeSort(list[mid:],index)
        merged = self.merge(left,right,index)
        return merged

    def merge(self, list1, list2, index):
        merged = []
        while len(list1) > 0 and len(list2) > 0:
            if float(list1[0][index]) <= float(list2[0][index]):
                merged.append(list1.pop(0))
            else:
                merged.append(list2.pop(0))

        if len(list1) > 0:
            merged += list1
        if len(list2) > 0:
            merged += list2

        return merged

    def quickSort(self,roomList,index):
        array = copy.deepcopy(roomList)
        
        if len(array) <= 1:
            return array
    
        pivot, tail = array[0], array[1:]
        
        leftSide = [x for x in tail if float(x[index]) <= float(pivot[index])]
        rightSide = [x for x in tail if float(x[index]) > float(pivot[index])]
        
        return self.quickSort(leftSide,index) + [pivot] + self.quickSort(rightSide,index)
    

class sort:

    def __init__(self,date=nowDate,locate=sejong):
        data = getData.getData()
        self.roomList = data.roomList(date,locate)
        self.monthlyList, self.charterList = data.devideRoom(date,locate) 
    def area(self,typeIndex, listType):
        index = 3
        areaS = ThreeSort()
        sorted = []
        if typeIndex == 1 and listType == 0:
            start = time.perf_counter()
            sorted = areaS.insertSort(self.roomList, index)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif typeIndex == 2 and listType == 0:
            start = time.perf_counter()
            sorted = areaS.mergeSort(self.roomList, index)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif typeIndex == 3 and listType == 0:
            start = time.perf_counter()
            sorted = areaS.quickSort(self.roomList, index)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif typeIndex == 1 and listType == 1:
            start = time.perf_counter()
            sorted = areaS.insertSort(self.roomList, index)
            end = time.perf_counter() - start
            return reversed(sorted), round(end, 3)
        elif typeIndex == 2 and listType == 1:
            start = time.perf_counter()
            sorted = areaS.mergeSort(self.roomList, index)
            end = time.perf_counter() - start
            return reversed(sorted), round(end, 3)
        elif typeIndex == 3 and listType == 1:
            start = time.perf_counter()
            sorted = areaS.quickSort(self.roomList, index)
            end = time.perf_counter() - start
            return reversed(sorted), round(end, 3)
        else:
            return
    def charter(self, typeIndex, listType):
        index = 6
        areaS = ThreeSort()
        sorted = []
        if typeIndex == 1 and listType == 0:
            start = time.perf_counter()
            sorted = areaS.insertSort(self.charterList, index)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif typeIndex == 2 and listType == 0:
            start = time.perf_counter()
            sorted = areaS.mergeSort(self.charterList, index)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif typeIndex == 3 and listType == 0:
            start = time.perf_counter()
            sorted = areaS.quickSort(self.charterList, index)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif listType == 1:
            start = time.perf_counter()
            sorted = areaS.mergeSort(self.charterList, index)
            end = time.perf_counter() - start
            return reversed(sorted), round(end, 3)
        else:
            return
    
    def monthly(self, typeIndex, listType):
        index = 5
        areaS = ThreeSort()
        sorted = []
        if typeIndex == 1 and listType == 0:
            start = time.perf_counter()
            sorted = areaS.insertSort(self.monthlyList, index)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif typeIndex == 2 and listType == 0:
            start = time.perf_counter()
            sorted = areaS.mergeSort(self.monthlyList, index)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif typeIndex == 3 and listType == 0:
            start = time.perf_counter()
            sorted = areaS.quickSort(self.monthlyList, index)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif listType == 1:
            start = time.perf_counter()
            sorted = areaS.mergeSort(self.monthlyList, index)
            end = time.perf_counter() - start
            return reversed(sorted), round(end, 3)

        else:
            return
    def construction(self, typeIndex, listType):
        index = 7
        areaS = ThreeSort()
        sorted = []
        if typeIndex == 1 and listType == 0:
            start = time.perf_counter()
            sorted = areaS.insertSort(self.monthlyList, index)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif typeIndex == 2 and listType == 0:
            start = time.perf_counter()
            sorted = areaS.mergeSort(self.monthlyList, index)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif typeIndex == 3 and listType == 0:
            start = time.perf_counter()
            sorted = areaS.quickSort(self.monthlyList, index)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif listType == 1:
            start = time.perf_counter()
            sorted = areaS.mergeSort(self.monthlyList, index)
            end = time.perf_counter() - start
            return reversed(sorted), round(end, 3)
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

    