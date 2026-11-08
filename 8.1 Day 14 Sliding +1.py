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

#trap water
#Given array of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining
b=[0,1,0,2,1,0,1,3,2,1,2,1]
left=0
right=len(b)-1
ans=0
leftMax=0
rightMax=0
while left<right:
    if b[left]<b[right]:
        if b[left]>=leftMax:
            leftMax=b[left]
        else:
            ans+=leftMax-b[left]
        left+=1
    else:
        if b[right]>=rightMax:
            rightMax=b[right]
        else:
            ans+=rightMax-b[right]
        right-=1
print(ans)