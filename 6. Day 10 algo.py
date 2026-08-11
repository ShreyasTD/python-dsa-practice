#1 selection sort
a=[1,2,3,4,50,90,-20]
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

#2.2 bubble sort
def bubble_sort(elements):
    size =len(elements)

    for i in range(size-1):
        swapped =False
        for j in range(size - i - 1):
            if elements[j] > elements[j + 1]:
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = tmp
                swapped =True
        if not swapped:
            break

if __name__ == "__main__":
    #elements = [5, 2, 1, 8, 4]
    elements = [1,3,5,2,4]
    bubble_sort(elements)
    print(elements)


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
   
#3.1  merge sort
# Merge two sorted lists

a = [1, 2, 3, 4]
b = [2, 4]

i = 0
j = 0
result = []

while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

while i < len(a):
    result.append(a[i])
    i += 1

while j < len(b):
    result.append(b[j])
    j += 1

print("MERGE RESULT:", result)
     
#3. Brute force approach
a=[1,2,3,5,6,7,8]
b=[2,3,4,5,6,7,8]
c=a+b
print(c)
c.sort()
print(c)
