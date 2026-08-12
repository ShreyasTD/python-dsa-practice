a=[1,2,8,4,9,6]
k=3
ans=0
for i in range(len(a)-k+1):
    subarraySum=0
    for j in range(i,i+k):
        subarraySum+=a[j]
    ans =max(ans,subarraySum)
print(ans)
