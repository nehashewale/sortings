'''We have seen how to implement insertion sort with integers.
Let's use insertion sort with custom objects. Create a Person class with 2 instance variables:
name and age. Let's sort a list of Person objects in ascending order based on their ages.'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __lt__(self,other):
        return self.age<other.age
    def __repr__(self):
        return str(self.name)
def Insertion_sort(poeple):
    for i in range(len(poeple)):
        j = i
        while j>0 and poeple[j-1]>poeple[j]:
            (poeple[j-1],poeple[j]) = (poeple[j],poeple[j-1])
            j = j-1
n = [Person('neha', 23), Person('pravinya', 17), Person('rani', 32), Person('praveen', 37)]
Insertion_sort(n)
print(n)
