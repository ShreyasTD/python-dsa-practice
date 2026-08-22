#Find Lower Bound - Find the first index where a[i] >=t
#a=[1,3,3,4]
#target = 3
#output : 1
def lb(a,t):
    left=0
    right=len(a)
    while left<right:
        mid = (left+right)//2
        if a[mid]>=t:
            right=mid
        else:
            left=mid+1
    return left

print(lb([1,2,3,3,4,5],3))

#Upper bound (first index where a[i]>target)
def ub(a,t):
    left=0
    right=len(a)
    while left<right:
        mid = (left+right)//2
        if a[mid]>t:
            right=mid
        else:
            left=mid+1
    return left



print(lb([3,5,7,8,9],5))

#create a function which returns the first and last ocurrence of a target in a list format 

#[foc,loc]

#find the minimum element in the rotated sorted list 
#[4,5,1,2,3]

def sum(arr,target):
    left =0
    right=len(arr)-1

    while left <right:
        if arr[left]+arr[right]==target:
            return[left,right]
        elif arr[left]+arr[right]<target:
            left+=1
        else:
            right -=1
    return[-1,-1]

print(sum([1,2,3,4,5],4))