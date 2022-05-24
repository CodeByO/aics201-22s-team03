# 이진탐색 + 선형탐색 이용하여 index 범위 구하기 + 해당 범위 print 하기 아직 api 데이터 대입 못함
#array: 크기 순서로 정렬된 배열
#index-> 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
array = [1,2,2,3,3,4,4,4,4,5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 8]
def binarySearch(array, num):   #num : 찾으려는 값
    left = 0
    right = len(array) - 1
    while(left <= right):
        middle = (left + right) // 2    #middle: 중간값 index
        if array[middle] == num:
            return middle
        elif array[middle] < num:
            left = middle + 1
        elif array[middle] > num:
            right = middle - 1
    return -1       #찾지 못하면  -1 return


min = binarySearch(array, 4)      #범위 검색의 작은값 (예시)
max = binarySearch(array, 8)      #범위 검색의 큰값 (예시)
i = min
k = max

def firstIndex(array, i):  #최소값이 시작하는 index 구하기
    if array[i] == array[i - 1]:
        while(array[i] == array[i - 1]):
            i = i - 1
        return i
    else:
        return i


def lastIndex(array, k):    #최대값이 시작하는 index 구하기
    if array[k] == array[len(array) -1]:
        return len(array) - 1      #array에서 가장 큰 값이면 마지막 (index - 1) return
    elif array[k] == array[k + 1]:
        while(array[k] == array[k + 1]):
            k = k + 1
        return k
    else:
        return k


print(firstIndex(array, i))     #작은 값이 시작하는 index print
print(lastIndex(array, k))      #큰 값이 끝나는 index print



for j in range(firstIndex(array,i),lastIndex(array,k) + 1, 1):      
    print(array[j])     #범위내의 모든 값 출력