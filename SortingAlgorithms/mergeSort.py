# Daha fazla tercih edilen bir algoritma -> nlogn
# Önce bizi verilen dizi her seferinde ikiye bölünerek tek tek parçalara ayrılır. Daha sonra bu parçalar ikili olarak karşılaştırılarak küçük olan sola gelerek birleştirilir.


# O(n)
def merge(arr1, arr2):
    firstPointer = 0
    secondPointer = 0
    mergedList = []

    while firstPointer < len(arr1) and secondPointer < len(arr2):
        if arr1[firstPointer] < arr2[secondPointer]:
            mergedList.append(arr1[firstPointer])
            firstPointer += 1
        else:
            mergedList.append(arr2[secondPointer])
            secondPointer += 1

    while firstPointer < len(arr1):
        mergedList.append(arr1[firstPointer])
        firstPointer += 1

    while secondPointer < len(arr2):
        mergedList.append(arr2[secondPointer])
        secondPointer += 1
    
    return mergedList

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    
    midPoint = int(len(arr)/2)
    leftPart = arr[:midPoint]
    rightPart = arr[midPoint:]
    return merge(mergeSort(leftPart), mergeSort(rightPart))

print(mergeSort([5,1,3,4,2,8,6,10]))