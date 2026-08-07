"""
#1 selection sort
a=[1,2,3,4,5,2,3,4,1]
for i in range (len(a)):
    minI=i
    for j in range (i+1, len(a)):
        if a[j]<a[minI]:
            minI=j
    a[i],a[minI]=a[minI],a[i]
print(a)

#2 Bubble sort
a=[1,2,3,2,3,6,7,8,6]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)

#3. Merge two sorted lists.
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merged = []
i, j = 0, 0
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1
merged.extend(list1[i:])
merged.extend(list2[j:])
print(merged)
"""
#3. Brute force approach
a=[1,2,3,5,6,7,8]
b=[2,3,4,5,6,7,8]
c=a+b
print(c)
c.sort()
print(c)