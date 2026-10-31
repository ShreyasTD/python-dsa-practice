"""
#finding index
a=[10,20,30,40,50,60]
for i in range(len(a)):
    if a[i]==50:
        print(i)
        break
  
#2sorting list in accending order
a=[1,4,5,0,-20,90,50]
a.sort()
print(a)

#3 reversing list in descending order
a=[1,2,3,4,50,90,-20]

a.reverse=True
print(a)

#4 reversing list
a=[1,2,3,4,50,90,20]
a.reverse()
print(a)


#5heking if an element is present in a list or not by taken input from user (membership operator)
a=[]
for i in range(5):
    a.append(int(input(f"enter the list of numbers: {i+1}")))
print(a)
if 50 in a:
    print("yes")
else:
    print("no")
 
#6 slicing of list
a=[10,20,30,40,50,60]
b=a[0:4]
print(b)
  
# syntax of a list to print the list by taking input from user
a = list(map(int, input().split()))
print(a)

#7print  sum of list
a = list(map(int, input().split()))
result=0
for i in a:
    result+=i
print(result)

#8 print even sum of list
a = list(map(int, input().split()))
result=0
for i in  a:
    if i%2==0:
        result+=i
print(result)

#9maximum number in a list
a = list(map(int, input().split()))
maxEle=-1
for i in a:
    if i>maxEle:
        maxEle=i
print(maxEle)

#10 minimum number in a list
a = list(map(int, input().split()))
minEle=10**10
for i in a:
    if i<minEle:
        minEle=i
print(minEle)

#11 print reverse of a list without using reverse function.
a = list(map(int, input().split()))
for i in range(len(a)-1, -1, -1):
    print(a[i], end=" ")

#12 frequency of an element in a list
a = list(map(int, input().split()))
x=int(input("enter the number to find frequency: "))
count=0
for i in a:
    if i==x:
        count+=1
print(count)

#13 reverse the frequency of an element in a list
a = list(map(int, input().split()))
b=[]
for i in range(len(a)-1, -1, -1):
    b.append(a[i])
print(b)
"""


"""
a=[3,4,5,6,2,6,8,3,5,6]
for i in range(len(a)):
    if a[i]==6:
        print(i)
        break
        """
"""        
a=[3,4,5,6,7,4,2]
a.sort(reverse=False)
print(a)
"""
"""
a=[3,4,5,6,9]
a.reverse()
print(a)
"""
"""
d=[6,3,6,4,3,2,5]
b=d[1:4]
print(b)

a=[3,4,5,6,3,2,7,8]
for i in range(len(a)):
    if a[i]==6:
     print(i)
     break
a=list(map(int,input().split()))   # taken n number of list
print(a)
"""

"""
# add all even number
a=list(map(int,input().split()))    # assign the every element as the int function or what ever taken the list to inistilize
result=0
for i in a:
    if i%2==0:
     result=result+i
print(result)
"""
a = list(map(int, input().split()))
maxEle=-1
for i in a:
    if i>maxEle:
        maxEle=i
print(maxEle)


a = list(map(int, input().split()))
minEle=10**10
for i in a:
    if i<minEle:
        minEle=i
print(minEle)

a = list(map(int, input().split()))
for i in range(len(a)-1, -1, -1):
    print(a[i], end=" ")

a = list(map(int, input().split()))
x=int(input("enter the number to find frequency: "))
count=0
for i in a:
    if i==x:
        count+=1
print(count)

a = list(map(int, input().split()))
b=[]
for i in range(len(a)-1, -1, -1):
    b.append(a[i])
print(b)

