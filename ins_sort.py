def Inserion_sort(list_a):
    iteration_len = range(1,len(list_a))
    for i in iteration_len:
        key = list_a[i]
        while list_a[i-1]>key and i>0:
            list_a[i-1],list_a[i] = list_a[i],list_a[i-1]
            i = i-1
    return list_a
print(Inserion_sort([9,5,3,-2,-9]))