def BubbleSort(list1):
    for i in range(len(list1)):
        for j in range(0,len(list1)-i-1):
            if list1[j]>list1[j+1]:
                temp = list1[j]
                list1[j]=list1[j+1]
                list1[j+1] = temp
                
l1 = [4,6,3,9,0,-1,-7]
BubbleSort(l1)
print(l1)
            
