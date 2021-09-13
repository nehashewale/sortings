def SelectionSort(array):
    for i in range(len(array)-1):
        min = i
        for j in range (i+1,len(array)):
            #if array[min]<array[j]: Decending order
            if array[j]<array[min]:
                min = j
        if min!= i:
            (array[min],array[i]) = (array[i],array[min])
data = [5,3,8,1,-6]
SelectionSort(data)
print(data)
