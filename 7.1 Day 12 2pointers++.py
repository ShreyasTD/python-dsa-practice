# 1Count the number of pairs in  a sorted list which sums to target.
"""a=[1,2,3,4,7,8,10]
left =0
right=len(a)-1
target =13
count=0

while left <right:
    if a[left] +a[right]== target:
        count+=1
        left+=1
        right-=1
     
    elif[a[left] +a[right]> target:
     right-=1
    
    else:
        left+=1

print(count)

#remove duplicates from an sorted arrray/list
a=[1,1,2,2,3]
res=[]
for i in a:
  if i not in res:
     res.append(i)
print(res)

# 2 slove and fast pointer tech
a=[1,2,2,2,3,3,4,5,5,6,6]
slow=0
for fast in range(1,len(a)):
   if a[fast]!=a[slow]:
      slow+=1
      a[slow]=a[fast]
print(a[:slow+1])

#3 Move all zeros in a list at the end without changing the order of elements
#Use Brute force first, later try optimizing the TC
a=[1,0,3,40,9,0]
nonZeroEle=[]
for i in a:
   if i!=0:
        nonZeroEle.append(i)
while len(nonZeroEle) <len(a):
   nonZeroEle.append(0)
print(nonZeroEle)
"""

"""
# 4 optimal approrch slow and fast
from turtle import reset


a=[1,2,0,9,8,0,12]
slow=0
for fast in range(len(a)):
   if a[fast]!=0:
     a[fast],a[slow]=a[slow],a[fast]
      #swap a(left) a(right):
     slow+=1
print(a)

#count the number of pairs in a sorted list which sums to target.
a=[1,2,3,4,7,8,10]
left =0
right=len(a)-1
target =13
count=0
while left <right:
      if a[left] +a[right]== target:
         count+=1
         left+=1
         right-=1
      
      elif a[left] +a[right]> target:
       right-=1
      
      else:
         left+=1
print(count)   

#remove duplicates from an sorted arrray/list
a=[1,1,2,2,3]
reset=[]
for i in a:
  if i not in reset:
     reset.append(i)
print(reset)
slow=0
for fast in range(1,len(a)):
   if a[fast]!=a[slow]:
      slow+=1
      a[slow]=a[fast]
print(a[:slow+1])

# Move all zeros in a list at the end without changing the order of elements
a=[1,0,3,40,9,0]
nonZeroEle=[]
for i in a:
   if i!=0:
        nonZeroEle.append(i)
while len(nonZeroEle) <len(a):
   nonZeroEle.append(0)
print(nonZeroEle)

a=[1,2,0,9,8,0,12]
slow=0
for fast in range(len(a)):
   if a[fast]!=0:
     a[fast],a[slow]=a[slow],a[fast]
      #swap a(left) a(right):
     slow+=1
print(a)
"""
"""
#find thw maximum sum of a subarray of size k
from ctypes import windll
import re


a=[1,2,8,4,9,6]
k=3
max_sum=0
for i in range(len(a)-k+1):
    current_sum=0
    for j in range(i,i+k):
        current_sum+=a[j]
    max_sum=max(max_sum,current_sum)
print(max_sum)

a=[1,2,8,4,9,6]
k=3
#SUM of first k elements
windowSum=0
for i in range(k):
    windowSum+=a[i]
ans=windowSum
for i in range(k,len(a)):
    newWindowSum=windowSum-a[i-k]+a[i]
    windowSum=newWindowSum
    ans=max(ans,newWindowSum)
print(ans)

#find the maximum sum of a subarray of size k
a=[1,2,8,4,9,6]
k=4
windowSum=0
for i in range(k):
    windowSum+=a[i]
    ans=windowSum
for i in range(k,len(a)):
    newWindowSum=windowSum-a[i-k]+a[i]
    windowSum=newWindowSum
    ans=max(ans,newWindowSum/k)
print(ans)

#find the length of smallest subarray with Sum>=target
a=[2,1,5,2,3,2]
target=7
left=0
current_sum=0
min_length=float('inf')
for right in range(len(a)):
    current_sum+=a[right]
    while current_sum>=target:
        min_length=min(min_length,right-left+1)
        current_sum-=a[left]
        left+=1
print(min_length)

"""
a=[2,3,1,2,4,3]
t=7
res=float('inf')
for i in range(len(a)):
   subArraySum=0
   for j in range(i,len(a)):
       subArraySum+=a[j]
       if subArraySum>=t:
             res=min(res,j-i+1)
print(res )