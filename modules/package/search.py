# from package import getData
from package import getData
from datetime import datetime
import time

#[Function] 자료구조를 이용한 검색 기능
#[DESC] 병합 정렬을 이용하여 정렬 후 입력 받은 값에 맞는 데이터 리턴
#[TODO] 정렬이 겹치므로 다른 정렬 고민
#[ISSUE] 한글은 검색을 어떻게 할지 고민

nowDate = datetime.today().strftime("%Y%m")
sejong = '36110'


class merge:

    def mergeSort(self, list, index):
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
            if int(list1[0][index]) <= int(list2[0][index]):
                merged.append(list1.pop(0))
            else:
                merged.append(list2.pop(0))

        if len(list1) > 0:
            merged += list1
        if len(list2) > 0:
            merged += list2

        return merged

    def mergeSort2(self, list, index, p, q):
        if p>=q:
            return
        mid  = (p + q) // 2
        self.mergeSort2(list, index, p, mid)
        self.mergeSort2(list, index, mid + 1, q)
        self.merge2(list, index, p, mid + 1, q)


    def merge2(self, list, index, left, right, end):
        merged = []
        l, r = left, right
        while l < right and r <= end:
            if int(list[l][index]) <= int(list[r][index]):
                merged.append(list[l])
                l +=1
            else:
                merged.append(list[r])
                r +=1
        while l < right:
            merged.append(list[l])
            l +=1
        while r <= end:
            merged.append(list[r])
            r+=1

        l = left
        for n in merged:
            list[l] = n	
            l +=1

class search:

    def __init__(self,date=nowDate,locate=sejong):
        data = getData.getData()
        self.roomList = data.roomList(date,locate)
    def rangeSearch(self, index, max, min):
        start = time.perf_counter()
        if(min > max):
            return
        result = []
        sort = merge()
        sortList = sort.mergeSort(self.roomList,index)
        for i in sortList:
            if int(min) <= int(i[index]) and int(max) >= int(i[index]):
                result.append(i)
            if int(max) < int(i[index]):
                break
        end = time.perf_counter() - start
        return result, end
    
    def matchSearch(self, index, value):
        start = time.perf_counter()
        result = []
        sort = merge()
        sortList = sort.mergeSort(self.roomList,index)
        for i in sortList:
            if int(value) == int(i[index]):
                result.append(i)
            if int(value) < int(i[index]):
                break
        end = time.perf_counter() - start
        return result, end

    def binarySearch(self, sorted, index, target, left, right):
        fined = []
        middle_idx = (left+right) // 2
        middle = sorted[middle_idx]
        print(middle)
        if int(target) == int(middle[index]):
            fined.append(middle)
        elif int(middle[index]) > int(target):
            self.binarySearch(sorted, index, target, left, middle_idx-1)
        elif int(middle[index]) < int(target):
            self.binarySearch(sorted, index, target, middle_idx+1, right)
        else: 
            return False

        return fined

if __name__ == '__main__':
    test = search('202203')
    result = test.rangeSearch(5,2006,1977)
    result2 = test.matchSearch(5,2004)
    for i in result:
        print(i)
    print("--------------------------------------------------------------------")
    for i in result2:
        print(i)

    bts = test.binarySearch(3,10,0)
    print(bts)

    # data = getData()
    # roomList = data.roomList('202203')
    # se = search('202203')
    # me = merge()
    # me.mergeSort2(roomList,5,0,len(roomList)-1)
    # bts = se.binarySearch(roomList,5,'1977',0,len(roomList)-1)
    # print(bts)
