#병합정렬(예시) api 데이터 적용 X
#len(array) : 14
array = [5,8,2,5,1,10,64,0,3,7,8,3,3,6]     #정렬할 데이터값 예시
def mergeSort(array):
    if len(array) > 1:      
        left = array[:len(array) // 2]
        right = array[len(array) // 2:]

        mergeSort(left)
        mergeSort(right)

        i = 0   #left index
        j = 0   #right index
        k = 0   #mergeSort index
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j = j + 1
            k = k + 1
        while i < len(left):
            array[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            array[k] = right[j]
            j = j + 1
            k = k + 1

    else:
        return -1


mergeSort(array)    
print(array)        #예시 array 정렬후 print
