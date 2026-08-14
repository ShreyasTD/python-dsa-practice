#Find the maximum sum of a subarray in a integer list kadan's algo
a=[1,2,3,4,5,6,-17,8,9,10]
ans=a[0]
subArraySum=0
for i in a:
    subArraySum+=i
    ans=max(ans,subArraySum)
    if subArraySum<=0:
        subArraySum=0
print(ans)


def greet ():
    print("hello")
greet() 

#parametter
def greet(name):
    print("hello",name)

greet('y')

def add(a,b):
    print(a+b)
add(2,3)

# Create a function which prints multiplication table of the number which is getting passed in the function as Parameter
def table(x):
    for i in range(1,11):
        print(x,"x",i,"x",x*i)
table(10)

def add(a,b):
    return a+b
#result=add(10,39)
#print(result)
print(add(2,3))

def add(a,b):
    return "i well not return the sum"
print(add(8,9))

#Create a function which returns the avg of a list passed as a parameter
def average(a):
    return sum(a)/len(a)
print(average([1,2,3,4]))

def scopeTest():
    x=10
    print(x)
scopeTest()
#print(x)

def greet(name="Defailt user"):
    print("hello",name)
greet()

#create a function to find max in a list
def maximum(a):
    return max(a)
numbers=[2,4,5,3,7,9]
print(maximum(numbers))

#create Bubble sort function and return the sorted list from it.
def bubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j+1]<a[j]:
                a[j+1],a[j]=a[j],a[j+1]
    return a
print(bubbleSort([2,3,1,4,2]))