"""
#1 avrage off sum
a = list(map(int, input().split()))
a=sum(a)/len(a)
print(a)

#2 count frequency of every element in a list
a = list(map(int, input().split()))
freq = {}
for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for key, value in freq.items():
    print(f"{key}: {value}")

#2.2 method 2 to count frequency of every element in a list

a = list(map(int,input().split()))
coveredItems = []
for i in a:
    if i in coveredItems:
        continue
    count = 0
    for j in a:
        if j==i:
            count+=1
    print(i, count)
    coveredItems.append(i)

#3 Check if the list given by user is Sorted or Not
a = list(map(int, input().split()))
is_sorted = True
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        is_sorted = False
        break
if is_sorted:
    print("The list is sorted.")
else:
    print("The list is not sorted.")

#4 find the last occurrence of an element given by user.
a = list(map(int, input().split()))
element = int(input("Enter the element to find the last occurrence: "))
last_occurrence = -1
for i in range(len(a)):
    if a[i] == element:
        last_occurrence = i
if last_occurrence != -1:
    print(f"The last occurrence of {element} is at index {last_occurrence}.")
else:
     print(f"{element} is not found in the list.")

#4.4 find the last occurrence of an element given by user.
a = list(map(int,input().split()))
num = int(input())
result = -1
for i in range(len(a)-1,-1,-1):
    if a[i]==num:
        print(i)
        break

#5 find the first occurrence of an element given by user.
a = list(map(int,input().split()))
num = int(input())
for i in range(len(a)):
    if a[i]==num:
        print(i)
        break
"""
#6 Rotate the list by 1 position to the right
a = list(map(int,input().split()))
lastEle = a[len(a)-1]
for i in range(len(a)-1,0,-1):
    a[i]=a[i-1]
a[0]=lastEle
print(a)