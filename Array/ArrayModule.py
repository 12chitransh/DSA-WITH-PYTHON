# # simple array with some important operation using array module

# import array as arr

# var = arr.array('i',[1,2,3,4,5])
# var.append(12)
# var.pop(2)
# var.insert(1,23)
# var.reverse()




# # for i in var :
# #     print(i , end=",")


# # copy = arr.array(var.typecode,(i for i in var))
# # print(copy)

# # taking input by user

from array import *

arr = array('i',[])
n = int(input("enter a number"))

for i in range(0,n):
    arr.append(int(input("enter a new number")))

for x in arr :
    print(x,end="") 
