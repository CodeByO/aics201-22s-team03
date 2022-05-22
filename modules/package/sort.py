import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


#[Function] 자료구조를 이용한 각 요소 정렬
#[DESC] 면적, 월세, 전세 각 분야를 3가지 정렬로 각각 정렬
#[TODO] 면적 정렬 추가 후 데이터는 어디서 넣어줄건지 고민

class areaSort:
    def insertSort(self,roomList, index):
        data = roomList
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

    def quickSort(self, roomList, first, final):
        
        data = roomList
        
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
        

        return data


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

    