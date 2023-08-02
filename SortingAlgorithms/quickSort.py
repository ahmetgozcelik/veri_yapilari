# İlk elemanı pivot olarak alır. Daha sonra o pivot noktasına göre küçükleri sola büyükleri sağa alarak devam eder. O pivot noktası yerini bulduktan sonra yeni satırdan pivot alınarak devam edilir ve hepsi yerini bulur.

def pivot(arr, pivotIndex, endIndex):
    swapIndex = pivotIndex
    for i in range(pivotIndex + 1, endIndex + 1):
        if arr[i] < arr[pivotIndex]:
            swapIndex += 1
            arr[swapIndex], arr[i] = arr[i], arr[swapIndex]
    arr[pivotIndex], arr[swapIndex] = arr[swapIndex], arr[pivotIndex]
    return swapIndex

def quickSort(arr, leftPointer = 0, rightPointer = None):
    if rightPointer == None:
        rightPointer = len(arr) - 1

    if leftPointer < rightPointer:
        swapIndex = pivot(arr, leftPointer, rightPointer)
        quickSort(arr, leftPointer, swapIndex - 1)
        quickSort(arr, swapIndex + 1, rightPointer)
    return arr

print(quickSort([5,1,3,4,2,8,6,10]))