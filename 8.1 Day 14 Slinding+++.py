a=[2,3,1,2,4,3]
left=0
ans=float('inf')
subArraySum=0
target=7
for right in range(len(a)):
    subArraySum+=a[right]
    while subArraySum>=target:
        ans=min(ans,right-left+1)
        subArraySum-=a[left]
        left+=1
print(ans)