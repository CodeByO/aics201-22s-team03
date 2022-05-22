# quickSort
import csv
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from package import getData


def quickSort(data, first, final):
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
    
    quickSort(data, first, high-1)
    quickSort(data, high+1, final)

       

    
if __name__ == '__main__':
    data = getData.getData()
    roomList = data.roomList('202203')

    quickSort(roomList, 0, len(roomList)-1)
    # for i in roomList:
    #     print(i[2])
    print(roomList)
    # print(i[index])
    # if __name__ == '__main__':
    #     a = [[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
    #     index = 2
    #     for i in range(len(a)):
    #         print(a[i][index]==a[i][index])

    #     print(a[2][index] == a[3][index])