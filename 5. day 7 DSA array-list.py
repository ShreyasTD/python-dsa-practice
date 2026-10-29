"""#1 using for loop
a=[10,20,30,40,50,-40,7]
for i in range(0,7):
 print(a[i], end=" ")

 #2 legth of list
a=[10,20,30,40,50,-40,7]
print(len(a))

#3 traversing list using for loop
a=[10,20,30,40,50,-40,7,40,50,60,70,80,90,100]
for i in a:
    print(i, end=" ")

#4 modifing elements of list
a=[10,20,30,40,50,-40,7]
a[4]=1
print(a)

#5 possision of element by odd number
a=[1,2,3,4,5,6,7,8,9,10]
for i in range (len(a)):
    if i%2==0:
        a[i]=-1
print(a)

#6 take a 10 input from the user and append it after every input in an empty list
list = []
for i in range(10):
    user_input = int(input(f"Enter a number {i+1}: "))
    list.append(user_input)
print(list)

#7 take 100 inputs from the user, append into a list and fund sum of all elements of  that list.
list = []
result = 0
for i in range(10):
    user_input = int(input(f"Enter a number {i+1}: "))
    list.append(user_input)
for i in range(len(list)):
    result += list[i]
print("The sum of all elements in the list is:", result)

#8 insert an element at a specific position in a list
a=[10,20,30,40,50,-40,7]
a.insert(3,100) #insert 100 at index 3
print(a)

#9 pop function to remove an element from a list
a=[10,20,30,40,50,-40,7]
a.pop()
print(a)

#10 remove function to remove an element from a list
a=[10,20,30,40,50,-40,7]
a.remove(10)
print(a)

#11 take 10 inputs , append in empty list, remove all elements which are divisible by 5
a=[1,2,3,4,5,6,7,8,9,10]
for i in a[:]:
    if i%5==0:
        a.remove(i)
print(a)
"""
"""
s=[1,2,3,45,True]
print(s)  #store the data in anyware

a=[1,2,3,4,5,-4]
print(a[1])     # accesing the list by last element by last indexing
"""
"""
a=[1,2,3,4,56,98]
for i in range(1,6):
    print(a[i])
                                #using in 
a=[1,2,3,4,5,6,8]
for i in a:
    print(i) 
"""

"""
ab=[2,3,3,4,45,54,5]
print(ab[-1])  
"""
"""
v=[2,3,5,4,1]
print(len(v))
"""
"""
a=[1,2,3,4,1,323,]     #Modifing element
a[5]=0
print(a)
"""
"""
b=[2,3,4,5,6,7,3,5,6,70]
for i in range(len(b)):
    if i%2==0:
      b[i]=-1
print(b)
                                """
"""                            
a=[1,2,3,4,5,7]
a.append(7)
print(a)
"""
"""
a = []
for i in range(10):
    num = int(input(f"Enter the number {i + 1}: "))     # f means dynamic data present in the set
    a.append(num)

print(a)
"""
"""
list = []
result = 0
for i in range(10):
    user_input = int(input(f"Enter a number {i+1}: "))
    list.append(user_input)
for i in range(len(list)):
    result += list[i]
print("The sum of all elements in the list is:", result)
"""
"""
a=[3,4,5,6,6]
a.insert(3,100)
print(a)
"""
"""
l=[9, 6,45, 6]
l.pop()
print(  l   )
"""
"""
d=[9,40,50,6]
d.remove(50)
print(d)
"""
a=[1,2,3,4,5,6,7,8,9,10]
for i in a[:]:
    if i%5==0:
        a.remove(i)
print(a)