#practice=1 factorial of a number using for loop
"""n=int(input("Enter a number: "))
fact=1
for i in range(1,n+1,1):
    fact *= i
print(fact)"""

#practice=2 nested loop to print a pattern
"""for i in range(1,5):
    for j in range(0,4):
        print(i,j)"""

#practice=3 square pattern using nested loop using *
"""n=int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()"""
#practice=4 number pattern using nested loop
"""n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(n):
        print(i,end=" ")
    print()
"""
#parctice=5 using while 
"""n=int(input("Enter a number: "))
for i in range(1,n+1):
    count=n
    while count>0:
        print(i,end=" ")
        count-=1    
    print()
"""
#practice=6  1234
"""n=int(input("Enter a number: "))
for i in  range(n):
    for j in range(1,n+1):
        print(j,end=" ")
    print()
"""

#practice=7   multiplication table using nested loop
"""n=int(input("Enter a number: "))
for i in range(1,n+1):
    print("table of",i)
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print()
"""
#practice=8  
n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()