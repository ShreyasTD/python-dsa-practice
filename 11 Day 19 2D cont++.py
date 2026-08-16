#1 create a function which returns the sum of primary diagonal elements on integer 2D list. for order of n
def primaryDiagnalSum(a):
    total=0
    for i in range(len(a)):
       total+=a[i][i]
    return total   

print(primaryDiagnalSum([[1,2,3],[4,5,6,],[7,8,9]]))

#2 for n^2
def primaryDiagnalSum(a):
    total=0
    for i in range(len(a)):
       for j in range(len(a[0])):
          if i==j:
            total+=a[i][j]
    return total
print(primaryDiagnalSum([[1,2,3],[4,5,6,],[7,8,9]]))

#2.1 print all the boundrey element in 2d list
def primaryDiagnalSum(a):
    total=0
    for i in range(len(a)):
       for j in range(len(a[0])):
          if i==0 or j==0 or i==len(a) or j==len(a[0]):
             return total
print(primaryDiagnalSum([[1,2,3],[4,5,6,],[7,8,9]]))

#3 Rotate a matrix by 90 deg clockwise
def rotateClockwise(a):
    for i in range(len(a)):
        for j in range(i+1,len(a[0])):
            a[i][j],a[j][i]=a[j][i],a[i][j]
    
    for i in range(len(a)):
        for j in range(len(a[0])-1,-1,-1):
            print(a[i][j],end=" ")
        print()

rotateClockwise([[1,2,3],[4,5,6],[7,8,9]])