from package import getData
from datetime import datetime
import time
import copy


#[Function] 자료구조를 이용한 각 요소 정렬
#[DESC] 면적, 월세, 전세 각 분야를 3가지 정렬로 각각 정렬
#[TODO] 면적 정렬 추가 후 데이터와 수행 시간 측정은 어디서 넣어줄건지 고민

nowDate = datetime.today().strftime("%Y%m")
sejong = '36110'

class areaSort:                                                                         #면적 정렬
    def insertSort(self,roomList):                                                      #삽입 정렬 구현
        """
        삽입정렬은 두번째 자료부터 시작하여 그 앞(왼쪽)의 자료들과 비교하여 삽입할 위치를 지정한 후 뒤로 옮기고
        지정한 자리에 자료를 삽입하여 정렬하는 알고리즘이다.
        --장점--
        1. 안정한 정렬 방법
        2. 레코드의 수가 적을 경우 알고리즘 자체가 매우 간단 -> 다른 복잡한 정렬 방법보다 유리할 수 있음
        3. 대부분의 레코드가 이미 정렬되어 있다면 매우 효율적일 수 있음
        --단점--
        1. 비교적 많은 레코드들의 이동을 포함
        2. 레코드 수가 많고 레코드 크기가 클 경우에 적합하지 않음.
        
        따라서 우리가 다루고 있는 자료(면적, 월세, 전세, 보증금 등)는 방대한 양의 자료를 정리해야 하기 때문에
        삽입정렬이 적합하지 않을꺼라 생각함.
        """
        data = copy.deepcopy(roomList)                                                  #roomList를 이용하여 데이터를 불러옴                          
        for j in range(1, len(data)):                                                   #데이터 전체를 범위로 지정
            for i in range(j, 0, -1):                                                   #데이터 왼쪽에서부터 정렬 시작
                if float(data[i][3]) < float(data[i-1][3]):                             #만약 오른쪽 데이터가 더욱 크다면
                    data[i], data[i-1] = data[i-1], data[i]                             #서로 데이터의 위치를 바꿈
                else:
                    break                                                               #i반복문을 통해 데이터가 하나씩 삽입정렬됨
        return data


    def mergeSort(self, roomList):                                                      #합병정렬
        """
        존 폰 노이만(John von Neumann)이 제안한 방법, 안정정렬에 속하며 분할 정복 알고리즘의 하나
        이때 분할 정복 방법은 문제를 작은 2개의 문제로 분리 후 각각 해결한 다음, 결과를 취합해 원래의 문제를 해결하는 전략이다.
        대개 순환 호출을 이용하여 구현한다.

        합병정렬 과정
        1. 리스트의 길이가 0 or 1 이면 이미 정렬된 것으로 본다. 그렇지 않은 경우에는
        2. 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
        3. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
        4. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.
        이때 합병정렬에서 실제로 정렬이 이루어지는 시점은 2개의 리스트를 합병(mgrge) 하는 단계이다.

        --장점--
        1. 안정적인 정렬 방법
        2. 데이터의 분포에 영향을 덜 받는다. 즉, 입력 데이터가 무엇이든 간에 정렬되는 시간(O(nlong2n))은 동일하다.
        3. 만약 레코드를 연결 리스트(Linked List)로 구성하면, 링크 인덱스만 변경되므로 데이터의 이동은 무시할 수 있을 정도로 작아진다.
           ㄴ> 제자리 정렬(in-place sorting)로 구현할 수 있다.
        4. 따라서 크기가 큰 레코드를 정렬할 경우에 연결 리스트를 사용한다면, 합병 정렬은 퀵 정렬을 포함한 다른 어떤 정렬보다 효율적이다.
        --단점--
        1. 만약 레코드를 배열(Array)로 구성하면, 임시 배열이 필요하다.
        2. 레코드들의 크기가 큰 경우 이동횟수가 많으므드로 매우 큰 시간적 낭비를 초래한다.

        정렬 알고리즘 시간복잡도를 비교했을 경우 구현하기에는 복잡하지만 효율적인 방법이라 할 수 있다.
        """
        data = copy.deepcopy(roomList)                                                  #데이터 호출
        if len(data) < 2:                                                               #만약 리스트의 길이가 2 미만이면 그냥 데이터를 리턴
            return data
        low = [[0]*5 for _ in range(500)]
        high = [[0]*5 for _ in range(500)]
        
            # 리스트 초기화
        

        middle = len(data) // 2 # data 길이 중간 값 취함                                 #합병 정렬을 위해 중간값을 찾아 저장

        low = self.mergeSort(data[:middle])                                             #나눠진 정렬의 low를 다시 합병 정렬
        high = self.mergeSort(data[middle:])                                            #나눠진 정렬의 high를 다시 합병정렬

        merged = []                                                                     #나눠져 정렬된 값을 합쳐 저장할 배열
        h = l = 0                                                                       #각각 정렬된 배열을 merge 에 넣어줄 순서를 배정

        while l < len(low) and h < len(high):                                           #low 와 high 두 배열을
            if float(low[l][3]) < float(high[h][3]):                                    #low 배열의 인자와 high 배열의 인자를 비교
                merged.append(low[l])                                                   #만약 low 배열의 인자가 작다면 merged에 저장 후
                l += 1                                                                  #다음 low 배열 인자와 비교
            else:                                                                       
                merged.append(high[h])                                                  #만약 아니라면 high 배열의 인자를 merged 에 저장후
                h += 1                                                                  #다음 high 배열 인자와 비교

        merged += low[l:]                                                               #인덱스 슬라이싱, while 문을 돌리고 남은 값들을 넣어주는 코드
        merged += high[h:]                                                              #인덱스 슬라이싱, while 문을 돌리고 남은 값들을 넣어주는 코드

        return merged                                                                   #정렬된 배열을 리턴


    def quickSort(self, roomList, first, final):                                        #퀵 정렬
        """
        찰스 앤터니 리처드 호어(Charles Antony Richard Hoare)가 개발한 정렬 알고리즘
        불완전 정렬에 ㅅ혹하며, 다른 원소와의 비교만으로 정렬을 수행하는 비교 정렬에 속함
        분할 정복 알고리즘의 하나로, 평균적으로 매우 빠른 수행 속도를 자라아하며 합병 정렬(merge sort)와는 달리 퀵정렬은 리스트를 비균등하게 분할한다.

        퀵 정렬 과정
        1. 리스트 안에 있는 한 요소를 선택한다. 이렇게 고른 원소를 피벗(pivot) 이라고 한다.
        2. 피서을 기준으로 피벗보다 작은 요소들은 모두 피벗 왼쪽으로 옮겨지고 피벗보다 큰 요소들은 모두 피벗 오른쪽으로 옮겨진다.
        ㄴ> 이때 피벗을 중심으로 왼쪽: 피벗보다 작은 요소, 오른쪽: 피벗보다 큰 요소들
        3. 피벗을 제외한 왼쪽 리스트와 오른쪽 리스트를 다시 정렬한다.
        ㄴ> 분할된 부분 리스트에 대하여 순환호출을 이용하여 정렬을 반복
        ㄴ> 부분 리스트에서도 다시 피벗을 정하고 피벗을 기준으로 2개의 부분 리스트로 나누는 과정을 반복한다.
        4. 부분 리스트들이 더 이상 분할이 불가능할 때까지 반복한다.

        --장점--
        1. 속도가 빠르다
        ㄴ> 시간복잡도(nlong2n)를 가지는 다른 정렬 알고리즘과 비교했을 때도 가장 빠르다
        2. 추가 메모리 공간을 필요로 하지 않는다.
        --단점--
        1. 정렬된 리스트에 대해서는 퀵 정렬의 불균형 분할에 의해 오히려 수행시간이 더 많이 걸린다.
        ㄴ> 퀵 정렬의 불균형 분할을 방지하기 위하여 피벗을 선택할 더욱 리스트를 균등하게 분할할 수 있는 데이터를 선택하면 어느정도 해소가 가능하다.

        따라서 많은 양의 데이터를 정렬해야 하기 때문에 현재 우리가 사용하는 자료 정렬에는 가장 적절하다고 생각한다.
        """
        data = copy.deepcopy(roomList)                                                  #api 데이터를 불러옴
        
        if first >= final:                                                              #?? 만약 배열의 첫번째가 마지막보다 클 경우 퀵 정렬을 수행 못함
            return
        
        pivot = first                                                                   #pivot은 처음에는 자료의 가장 처음 자료로
        low = first + 1                                                                 #pivot 바로 앞의 자료부터
        high = final                                                                    #끝까지 자료를 정렬

        while low <= high:                                                              #low의 값이 high 값보다 작거나 같을때까지
            while low <= final and float(data[low][3]) <= float(data[pivot][3]):        #low의 값이 final보다 작고, 데이터값이 pivot 값보다 작거나 같다면
                low +=1                                                                 #low 값을 1증가
            while high>first and float(data[high][3]) >= float(data[pivot][3]):         #high 값이 first값보다 크고, 데이터값이 piovt 값보다 크거나 같다면
                high -= 1                                                               #high 값을 1증가
            if low > high:                                                              #만약 low > high 일 경우
                data[high],data[pivot] = data[pivot],data[high]                         #high -> pivot , pivot -> high 저장 (swap 과 유사)
            else:
                data[low],data[high]=data[pivot],data[low]                              #low -> pivot , high -> low 저장 (swap 과 유사)
        
        self.quickSort(data, first, high-1)                                             #재귀로 리스트들이 더이상 분할이 안될때까지 반복
        

        return data

class sort:

    def __init__(self,date=nowDate,locate=sejong):                                       #데이터를 불러옴
        data = getData.getData()
        self.roomList = data.roomList(date,locate)
        self.monthlyList, self.charterList = data.devideRoom(date,locate)
    def area(self,index):
        areaS = areaSort()                                                               #클래스 선언
        sorted = []
        if index == 1:                                                                   #index 값이 1일 경우 insertSort 실행
            start = time.perf_counter()
            sorted = areaS.insertSort(self.roomList)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif index == 2:                                                                 #index 값이 2일 경유 mergeSort 실행
            start = time.perf_counter()
            sorted = areaS.mergeSort(self.roomList)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        elif index == 3:                                                                 #index 값이 3일 경우 quickSort 실행
            start = time.perf_counter()
            sorted = areaS.quickSort(self.roomList, 0, len(self.roomList)-1)
            end = time.perf_counter() - start
            return sorted, round(end, 3)
        else:
            return
    def deposit(self):
        pass
    
    def monthly(self):
        pass


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

    