#given array a, print prefix sum array
"""a=[2,1,3,4,4,9]
for i in range(1,len(a)):
    a[i]+=a[i-1]

print(a)
"""
#find the pivot element index
a=[1,2,3,2,3,4,5,6]
for i in range(len(a)):
    leftSum=0
    rightSum=0
    for j in range(i):
        leftSum+=a[j]
    for j in range(i+1, len(a)):
        rightSum+=a[j]
    if leftSum==rightSum:
        print(i)
"""
#find frequency of every element in an int list.
a=[1,2,1,3,4,2,3,4,1]
freq={}
for i in range(len(a)):
    if a[i] in freq:
      freq[a[i]]+=1
    else:
        freq[a[i]]=1

print(freq)
"""
