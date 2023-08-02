# İkinciyi direkt dışarı alır. Daha sonra birinciyle kıyaslar ve küçükse yer değiştirir. Sonra üçüncü dışarı alınır ve ikinciyle kıyaslanır. Bu şekilde devam eder.

def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while temp < arr[j] and j > -1:
            arr[j+1] = arr[j]
            arr[j] = temp
            j -= 1
    return arr

print(insertionSort([5,1,3,4,2,8,6,10]))            