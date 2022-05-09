
# quickSort
data = [3,1,6,4,2,7,0,9]

def quickSort(data):
    if len(data) > 2:
        return data

    pivot = data[0]
    result = []
    low = []
    high = []

    for i in range(1, len(data)):
        if pivot > data[i]:
            low.append(data[i])
        else:
            high.append(data[i])
    
    low.sort()
    high.sort()

    print(low)
    print(pivot)
    print(high)
