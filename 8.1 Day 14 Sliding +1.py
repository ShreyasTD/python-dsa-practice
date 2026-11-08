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
h=[2,4,8,9,3,1,16,4,2,3,5,7,8]
left=0
right=len(h)-1
ans=0
leftMax=0
rightMax=0
while left<right:
    if h[left]<h[right]:
        if h[left]>=leftMax:
            leftMax=h[left]
        else:
            ans+=leftMax-h[left]
        left+=1
    else:
        if h[right]>=rightMax:
            rightMax=h[right]
        else:
            ans+=rightMax-h[right]
        right-=1
print(ans)