
def Insertion_Sort1(array_list1):
    for i in range(len(array_list1)):
        j = i
        while j>0 and array_list1[j-1]>array_list1[j]:
            (array_list1[j-1],array_list1[j]) = (array_list1[j],array_list1[j-1])
            j = j-1 
data1 = [5,7,6,2,3,98,1]
Insertion_Sort1(data1)
print(data1)