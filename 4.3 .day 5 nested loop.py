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
"""
#practice=8  
n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

"""

                                                 #fact of number using for loop

"""
n=int(input("Enter a number: "))
fact=1
for i in range (1,n+1):
    fact*=i
print(fact)

#using while loop

n=int(input("Enter a number: "))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print(fact)

"""
"""
#Nested for loop
for i in range(0,6):
    for j in range(0,4):
        print(i,j)
"""

"""
input=int(input("Enter the number which you want to print as the square pattern: "))
for i in range(0,input):
    for j in range(0,input):
        print("*",end=" ")
    print()
"""
"""
num=int(input("enter the number : "))
for i in range (1,num+1):
    for j in range(1,i+1):
        print(num,end=" ")
    print()
"""
"""
n=int(input("enter the number : " ))
for i in range(1,n+1):
    for j in range (n):
        print(i,end=" ")
    print()
"""
# inner loop is while loop
"""
n=int(input("Enter the number : " ))
for i in range(1,n+1):
    count= 0
    while count<n:
        print(i,end=" ")
        count+=1
    print()

                                              #or
n=int(input("Enter the number : " ))
for i in range(1,n+1):
    count= n
    while count>0:
        print(i,end=" ")
        count-=1
    print()

n=int(input("Enter the number : " ))
for i in range(n):
    for j in range(1,n+1):
        print(j,end=" ")
    print() 

"""
"""
#take user input N, print multiplication table of 1 to N using nested loop
n=int(input("Enter the number : " ))
for i in range(1,n+1):
    print(f"Multiplication table of {i}:")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print()
"""
         #right angle triangle pattern using nested loop for same number
"""
n=int(input("Enter the number : " ))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n,end=" ")
    print()
     """
          #right angle triangle pattern using nested loop for 1 to n number

n=int(input("Enter the number : " ))
for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
