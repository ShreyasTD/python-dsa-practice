
#banarey serch

#create a function which takes a sorted list and a target and returns a Boolean (T/F) if the target exist in the list.
def bs(a,target):
    left=0
    right = len(a)-1
    found = False
    while left<=right:
        mid=(left+right)//2
        if a[mid]==target:
            found=True
            return found
        elif a[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return found

print(bs([1,2,3,4,5],2))

#Find the first occurence of target in a sort list.
#[1,2,2,5,6,77,77,100], target = 77
#output :  5

def firstOccurence(a,target):
    left=0
    right = len(a)-1
    ans=-1
    while left<=right:
        mid=(left+right)//2
        if a[mid]==target:
            ans=mid
            right=mid-1
        elif a[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return ans

print(firstOccurence([1,2,3,3,3,3,3,4],2))

#return the last occurence of target in a sorted list
def lastOccurence(a,target):
    left=0
    right = len(a)-1
    ans=-1
    while left<=right:
        mid=(left+right)//2
        if a[mid]==target:
            ans=mid
            left=mid+1
        elif a[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return ans


print(lastOccurence([1,2,3,3,3,3,3,4],3))

#create a function which returns the index where a target should be inserted in a sorted list.

#function parameters : a sorted list , target

  