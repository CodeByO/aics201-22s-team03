import csv
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from package import getData

class sort:
    def insertSort(self, data, index):
        for j in range(1, len(data)):
            for i in range(j, 0, -1):
                if float(data[i][2]) < float(data[i-1][2]):
                    data[i], data[i-1] = data[i-1], data[i]
                else:
                    break
        return data

    def mergeSort(self, data, index):
        if len(data) < 2:
            return data
        low = [[0]*5 for _ in range(500)]
        high = [[0]*5 for _ in range(500)]
        
            # 리스트 초기화
        
        # if len(data) < 2:
        #     return data
        middle = len(data) // 2 # data 길이 중간 값 취함    

        low = self.mergeSort(data[:middle], 2)
        high = self.mergeSort(data[middle:], 2)   

        merged = []
        h = l = 0
        # for i in range(1, len(data)):
        while l < len(low) and h < len(high):
            if float(low[l][2]) < float(high[h][2]):
                merged.append(low[l])
                l += 1
            else:
                merged.append(high[h])
                h += 1

        merged += low[l:]
        merged += high[h:]

        return merged

    def quickSort(self, data, first, final):
        if first >= final:
            return
        
        pivot = first
        low = first + 1
        high = final

        while low <= high:
            while low <= final and float(data[low][2]) <= float(data[pivot][2]):
                low +=1
            while high>first and float(data[high][2]) >= float(data[pivot][2]):
                high -= 1
            if low > high:
                data[high],data[pivot] = data[pivot],data[high]
            else:
                data[low],data[high]=data[pivot],data[low]
        
        self.quickSort(data, first, high-1)
        self.quickSort(data, high+1, final)


if __name__ == '__main__':
    s = sort()
    data = getData.getData()
    roomList = data.roomList()
    newd=s.mergeSort(roomList, 2)
    s.quickSort(roomList, 0, len(roomList)-1)
    s.insertSort(roomList, 2)

    print('----------------mergeSort-------------------')

    for i in newd:
        print(i[2])
    
    print('----------------quickSort-------------------')

    # for i in roomList:
    #     print(i[2])

    print('----------------insertSort-------------------')

    for i in roomList:
        print(i[2])