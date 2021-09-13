def Merge_sort(arrayList):
    if len(arrayList) == 1:
        return
    middle_index = len(arrayList)//2
    left_half = arrayList[:middle_index]
    right_half = arrayList[middle_index:]
    Merge_sort(left_half)
    Merge_sort(right_half)
    i = 0
    j = 0
    k = 0
    while i < len(left_half) and j< len(right_half):
        if left_half[i] < right_half[j]:
            arrayList[k] = left_half[i]
            i = i+1
        else:
            arrayList[k] = right_half[j]
            j = j+1
        k = k+1
    while i < len(left_half):
        arrayList[k] = left_half [i]
        i =i+1
        k = k+1
    while j< len(right_half):
        arrayList[k] = right_half[j]
        j = j+1
        k = k+1 


data = [7,6,9,8,79,44,53,75,99,]
Merge_sort(data)
print(data)