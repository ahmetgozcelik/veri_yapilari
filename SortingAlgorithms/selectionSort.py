# Sıradan işaretlediği en küçük değerle önüne çıkan hepsini işaretlediği ile karşılaştırıyor ve karşısına daha küçük bir değer çıkarsa onu işaretliyor. Sona gelince en küçüğü başa atıyor.

def selectionSort(arr):
    for i in range(len(arr) - 1):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if i != minIndex:
             arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

print(selectionSort([5, 1, 3, 4, 2, 8, 6, 10]))
