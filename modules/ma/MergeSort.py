# MergeSort
import csv
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from package import getData

def mergeSort(data, index):
    if len(data) < 2:
        return data
    low = [[0]*5 for _ in range(500)]
    high = [[0]*5 for _ in range(500)]
    
        # 리스트 초기화
    
    # if len(data) < 2:
    #     return data
    middle = len(data) // 2 # data 길이 중간 값 취함    

    low = mergeSort(data[:middle], 2)
    high = mergeSort(data[middle:], 2)   

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




if __name__ == '__main__':
    data = getData.getData()
    roomList = data.roomList('202203')
    data= mergeSort(roomList, 2)
    for i in data:
        print(i[2])
    # print(i[index])
    # if __name__ == '__main__':
    #     a = [[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
    #     index = 2
    #     for i in range(len(a)):
    #         print(a[i][index]==a[i][index])

    #     print(a[2][index] == a[3][index])