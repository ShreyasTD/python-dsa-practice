#find the sum of evry subarray of size k for brute force method
"""a=[1,2,8,4,9,6]
k=3
ans=0
for i in range(len(a)-k+1):
    subarraySum=0
    for j in range(i,i+k):
        subarraySum+=a[j]
    ans =max(ans,subarraySum)
print(ans)

# by optimal solustion
a=[1,2,8,4,9,6]
#sum of 1st window
windowSum=0
for i in range(k):
    windowSum+=a[i]
sum=windowSum
for i in range(k,len(a)):
    newWindowSum=windowSum-a[i-k] +a[i]
    windowSum=newWindowSum
    ans=max(ans,windowSum)
print(ans)
"""
#Find maximum avg subarray value of size k brute force method
a=[2,3,1,2,4,3]
t=5
res=float('inf')
for i in range(len(a)):
   subArraySum=0
   for j in range(i,len(a)):
      subArraySum+=a[j]
      if subArraySum>=t:
         res=min(res,j-i+1)
print(res)
#Find the length of Smallest Subarray with Sum>=Target