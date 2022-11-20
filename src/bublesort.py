#taking list of numbers as an argument in function bubblesort
def bubble_sort(l):
#iterating through each  number in list l
    for i in range(len(l)):
#comparing first picked number and storing it out in a variable 
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                # l[j],l[j+1]=l[j+1],l[j]
                temp = l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    return l
print(bubble_sort([2,3,6,1]))
