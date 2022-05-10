# MergeSort
import csv
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from package import getData

def mergeSort(data, index):
    
    result = [[0]*5 for _ in range(1000)]
    low = [[0]*5 for _ in range(500)]
    high = [[0]*5 for _ in range(500)]
    middle = len(data) // 2
    pivot = data[middle]
    for i in range(1, len(data)):
        if float(pivot[2]) > float(data[i][2]):
            low.append(data[i])
        else:
            high.append(data[i])
    
    low = mergeSort(data[:middle], 2)
    high = mergeSort()

    print(low)


if __name__ == '__main__':
    data = getData.getData()
    roomList = data.roomList('202203')
    index = 2

    mergeSort(roomList, index)

    # print(i[index])
    # if __name__ == '__main__':
    #     a = [[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
    #     index = 2
    #     for i in range(len(a)):
    #         print(a[i][index]==a[i][index])

    #     print(a[2][index] == a[3][index])