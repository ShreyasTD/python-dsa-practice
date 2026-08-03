#1 practice problem for *
"""n=int(input("Enter the n"))
for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" " )
    print()


#2nd practice
n=int(input("Enter the n "))
for i in range (1,n+1):
    start=n
    for j in range (i):
        print(start, end=" ")
        start-=1
    print()

#3rd practice
n=int(input("Enter the n "))
for i in range (0,n+1):
    for j in range(n,n-i,-1):
        print(j, end=" ")
    print()

#4th practice

x1=int(input("Enter the x1 "))
y1=int(input("Enter the y1 "))
x2=int(input("Enter the x2 "))
y2=int(input("Enter the y2 "))
for i in range (x1,x2+1):
    for j in range (y1,y2+1):
        print(i,j, end=" ")


n=1000
for i in range (1,n+1):
    for j in range (1,i+1):
        if i%j==0:
         print(j, end=" ")
    print()
    
n=int(input("Enter the n "))
for i in range (1,n+1):
    for j in range (i):
         print("x", end=" ")
"""
n=int(input("Enter the n "))
for i in range (n-1,0,-1):
    for j in range (i):
         print("x", end=" ")
    print()