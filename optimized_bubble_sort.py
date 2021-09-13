def BubbleSort(l1):
    for i in range(len(l1)):
        swapped = False
        for j in range (0,len(l1)-i-1):
            if l1[j]>l1[j+1]:
                temp  = l1[j]
                l1[j] = l1[j+1]
                l1[j+1] = temp 
                swapped = True
        if not swapped:
            break
data = [-2,45,0,11,5]
BubbleSort(data)
print(data)