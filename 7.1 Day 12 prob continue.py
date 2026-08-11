#Count the number of pairs in  a sorted list which sums to target.
"""a=[1,2,3,4,5,6,7,8,9,10]
left =0
right=len(a)-1
target =15
count=0

while left <right:
    if a[left] +a[right]== target:
        count+=1
        left+=1
        right+=1
     
    elif[left] +a[right]> target:
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

#slove and fast pointer tech
a=[1,2,2,2,3,3,4,5,5,6,6]
slow=0
for fast in range(1,len(a)):
   if a[fast]!=a[slow]:
      slow+=1
      a[slow]=a[fast]
print(a[:slow+1])

#Move all zeros in a list at the end without changing the order of elements
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
#optimal approrch
a=[1,2,0,9,8,0,12]
slow=0
for fast in range(len(a)):
   if a[fast]!=0:
     a[fast],a[slow]=a[slow],a[fast]
      #swap a(left) a(right):
     slow+=1
print(a)