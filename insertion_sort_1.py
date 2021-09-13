def Insertion_sort(array_list):
    for j in range(1,len(array_list)):
        key = array_list[j]
        i = j-1
        while i>=0 and array_list[i]>key:
            array_list[i+1] = array_list[i]
            i = i-1
        array_list[i+1] = key
data = [5,3,7,2,1]
Insertion_sort(data)
print(data)