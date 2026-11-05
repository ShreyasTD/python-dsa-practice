"""# 1. Check if a pair in a sorted list sums to 100 by brute force approach
a=[1,2,3,40,50,50,90]
target=100
isfound=False
for i in range (len (a)):
    for j in range (i+1,len(a)):
        if a[i]+a[j]==target:
            isfound=True
            break

    if isfound==True:
        break
print(isfound)

# 2. check if a pair in a sorted list  by optimized approach
a=[1,2,3,40,50,60]
left =0
target=100
right=len(a)-1
isfound=False
while left<right:
     if a[left]+a[right]==target:
         isFound=True
         break
     elif a[left]+a[right]<target:
         left=left+1
     else:
        right=right-1
print(isfound)
"""
"""
# 3. Check if list given by users is palindromic or not?
#TC : 1 2 2 1 1 2 2 1 - True
#TC2: 1 1 2 1 2 1 - False
a = [1,1,2,3,2,1,1]
left = 0
right = len(a)-1
isPali= True
while left<right:
    if a[left]==a[right]:
        left+=1
        right-=1
    else:
        isPali=False
        break
print(isPali)

# reverse a list using 2 pointers.
a = [1,1,2,3,2,1,6]
left = 0
right = len(a)-1
while left<right:
    a[left],a[right] = a[right], a[left]
    left+=1
    right-=1
print(a)

#Find all the pairs which sums to a target.
a = [1,2,3,4,5,6]
left = 0
right = len(a)-1
target = 8
while left<right:
    if a[left]+a[right]==target:
        print(a[left], a[right])
        left=left+1
        right=right-1
    elif a[left]+a[right]>target:
        right-=1
    else:
        left+=1

from unittest import result
"""
#two sorted lists merge into one sorted list and find the edge case where one list is empty.
a=[1,3,5]
b=[2,4]
i=0
j=0
result=[]
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        result.append(a[i])
        i+=1
    else:
        result.append(b[j])
        j+=1
while i<len(a):
    result.append(a[i])
    i+=1
while j<len(b):
    result.append(b[j])
    j+=1
print(result)

#check if a pair in a sorted list sums to 100 or not
a = [1, 2, 3, 40, 50, 60]
left = 0
right = len(a) - 1
target = 100
isfound = False
while left < right:
    if a[left] + a[right] == target:
        isfound = True
        break
    elif a[left] + a[right] < target:
        left += 1
    else:
        right -= 1
print(isfound)

      # brute force approach
a=[1, 2, 3, 40, 50, 60]
target=100
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==target:
            isfound=True
            break
    if isfound==True:
        break
print(isfound)

#optimized approach to find all pairs which sums to a target.
a = [1, 2, 3, 40, 50, 60]
left = 0
right = len(a) - 1
target = 100
isfound = False
while left < right:
    if a[left] + a[right] == target:
        print(a[left], a[right])
        isfound = True
        left += 1
        right -= 1
    elif a[left] + a[right] < target:
        left += 1
    else:
        right -= 1
print(isfound)

#check if a list is palindromic or not.
a = [7,1, 2, 3, 2, 1,7]
left = 0
right = len(a) - 1
isPali = True
while left < right:
    if a[left] == a[right]:
        left += 1
        right -= 1
    else:
        isPali = False
        break
print(isPali)

#reverse a list using 2 pointers.
a = [1, 2, 3, 4, 5, 6]
left = 0
right = len(a) - 1
while left < right:
    a[left], a[right] = a[right], a[left]
    left += 1
    right -= 1
print(a)

#find all the pairs which sums to a target.
a = [1, 2, 3, 4, 5, 6]
left = 0
right = len(a) - 1
target = 8
while left < right:
    if a[left] + a[right] == target:
        print(a[left], a[right])
        left += 1
        right -= 1
    elif a[left] + a[right] > target:
        right -= 1
    else:
        left += 1
