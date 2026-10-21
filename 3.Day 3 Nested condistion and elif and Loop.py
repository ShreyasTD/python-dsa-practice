'''
marks=int(input("Enter your marks: "))
if marks>=90:
    print("Grade A")
elif marks>=85:
    print("Grade B")
elif marks>=75:
    print("Grade C")
else:
    print("fail")
'''
"""
a=int(input("Enter a number: "))
if a>0:
    if a%2==0:
        print(f"{a} is positive and even")
    else:
        print(f"{a} is positive and odd")
else:
    print(f"{a} is not positive")
"""

"""
a=int(input("Enter the number: "))
if a>0:
    if a%2==0:
        print(f"{a} is positive and even")
    else:
        print(f"{a} is positive and odd")
else:
    print(f"{a} is not positive")
"""
"""
x=10
if x>5:
    if x<20:
        print("done")

"""
#loops
"""
start=1
while start<=100:
          print(start)
          start+=1
print("done")

"""
'''
start=1
while start<=1000:
    if start%2==1:
        print(start)
    start+=1
'''
"""
start=100
while start>=1:
    print(start)
    start-=1
print("done")

"""
"""
table=int(input("Enter the number for table: "))
start=1
while start<=10:
    print(f"{table} * {start} = {table*start}")
    start+=1
print("done")
"""

result=0
start=1
while start<=100:
    result = result + start
    start+=1
print(result)