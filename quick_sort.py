def QuickSort(arraylist):
    length = len(arraylist)
    if length <= 1:
        return arraylist
    else:
        pivot = arraylist.pop()
    items_lower = []
    items_grater =[]
    for item in arraylist:
        if item > pivot:
            items_grater.append(item)
        else:
            items_lower.append(item)
    return QuickSort(items_lower) + [pivot] +QuickSort(items_grater)

list1 = [8,7,6,1,0,9,2]
print(QuickSort(list1))


