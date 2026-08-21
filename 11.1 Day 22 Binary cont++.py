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

