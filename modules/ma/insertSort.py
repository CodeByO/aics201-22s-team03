# insertSort
import csv
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from package import getData

def insertSort(data, index):
    for j in range(1, len(data)):
        for i in range(j, 0, -1):
            if float(data[i][2]) < float(data[i-1][2]):
                   data[i], data[i-1] = data[i-1], data[i]
            else:
                   break
    return data

if __name__ == '__main__':
    data = getData.getData()
    roomList = data.roomList('202203')
    index = 2 
    insertSort(roomList, 2)
    
    for i in roomList:
        print(i[2])
    