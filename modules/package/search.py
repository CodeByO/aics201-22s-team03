from package import getData
#from getData import getData
from datetime import datetime
import time
import copy
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
            if list1[0][index] <= list2[0][index]:
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
        #data = getData()
        self.roomList = data.roomList(date,locate)
        self.filterList = self.giveFilter()
    def rangeSearch(self, index, max, min, wordList):
        start = time.perf_counter()
        
        if(min > max):
            return
        result = []
        locate = wordList[0] if wordList[0] != '0' else None
        court = wordList[1] if wordList[1] != '0' else None
        division = wordList[2] if wordList[2] != '0' else None
        filteredList = copy.deepcopy(self.roomList)
        if locate != None:
            filteredList = [x for x in filteredList if locate == x[0]]
        if court != None:
            filteredList = [x for x in filteredList if court == x[1]]
        if division != None:
            filteredList = [x for x in filteredList if division == x[2]]
        try:
            if index > 2 and len(filteredList) > 0:
                sort = merge()
                sortList = sort.mergeSort(filteredList,index)
                for i in sortList:
                    if int(min) <= int(i[index]) and int(max) >= int(i[index]):
                        result.append(i)
                    if int(max) < int(i[index]):
                        break
            else:
                result = filteredList
        except:
            return None, None
        end = time.perf_counter() - start
        return result, round(end, 3)
    
    def matchSearch(self, index, value, wordList):
        start = time.perf_counter()
        result = []
        locate = wordList[0] if wordList[0] != '0' else None
        court = wordList[1] if wordList[1] != '0' else None
        division = wordList[2] if wordList[2] != '0' else None
        filteredList = copy.deepcopy(self.roomList)
        if locate != None:
            filteredList = [x for x in filteredList if locate == x[0]]
        if court != None:
            filteredList = [x for x in filteredList if court == x[1]]
        if division != None:
            filteredList = [x for x in filteredList if division == x[2]]
        
        try:
            if index > 2 and len(filteredList) > 0:
                sort = merge()
                sortList = sort.mergeSort(filteredList,index)
                for i in sortList:
                    if value == i[index]:
                        result.append(i)
                    if value < i[index]:
                        break
            else:
                result = filteredList
        except:
            return None, None
        end = time.perf_counter() - start
        return result, round(end, 3)

    def giveFilter(self):

        locateList = []
        courtList = []
        divisionList = []

        locateList.append(self.roomList[0][0])
        courtList.append(self.roomList[0][1])
        divisionList.append(self.roomList[0][2])

        for i in self.roomList:
            if i[0] not in locateList:
                locateList.append(i[0])
            if i[1] not in courtList:
                courtList.append(i[1])
            if i[2] not in divisionList:
                divisionList.append(i[2]) 
        self.bubble(locateList)
        self.bubble(courtList)
        self.bubble(divisionList)
        
        filterList = [locateList, courtList, divisionList]
        
        return filterList

    def bubble(self,roomList):
        for i in range(len(roomList) - 1, 0, -1):
            for j in range(i):
                if roomList[j] > roomList[j+1]:
                    roomList[j], roomList[j + 1] = roomList[j + 1], roomList[j]
if __name__ == '__main__':
    date = '202112'
    locate = ['36110','11110','27110']
    test = search(date,locate)
    filterList = test.giveFilter()
    for i in filterList:
        print(i)
    # data = getData()
    # roomList = data.roomList('202203')
    # se = search('202203')
    # me = merge()
    # me.mergeSort2(roomList,5,0,len(roomList)-1)
    # bts = se.binarySearch(roomList,5,'1977',0,len(roomList)-1)
    # print(bts)
