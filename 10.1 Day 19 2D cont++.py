#1 create a function which returns the sum of primary diagonal elements on integer 2D list. for order of n
def primaryDiagnalSum(a): # type: ignore
    total=0
    for i in range(len(a)):
       total+=a[i][i]
    return total   

print(primaryDiagnalSum([[1,2,3],[4,5,6,],[7,8,9]]))

#2 for n^2
def primaryDiagnalSum(a): # type: ignore
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
def rotateClockwise(a): # type: ignore
    for i in range(len(a)):
        for j in range(i+1,len(a[0])):
            a[i][j],a[j][i]=a[j][i],a[i][j]
    
    for i in range(len(a)):
        for j in range(len(a[0])-1,-1,-1):
            print(a[i][j],end=" ")
        print()

rotateClockwise([[1,2,3],[4,5,6],[7,8,9]])


#4. Print Anticlockwise rotation of a 2d

def rotateClockwise(a):
    for i in range(len(a)):
        for j in range(i,len(a[0])):
            a[i][j],a[j][i]=a[j][i],a[i][j]
    
    for i in range(len(a)-1,-1,-1):
        for j in range(len(a[0])):
            print(a[i][j],end=" ")
        print()


rotateClockwise([[1,2,3],[4,5,6],[7,8,9]])

#5. Print spiral traversal of a matrix.
a=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]


direction="right"
topBoundary=0
bottomBoundary=len(a)-1
leftBoundary = 0
rightBoundary = len(a[0])-1


while leftBoundary<=rightBoundary and topBoundary<=bottomBoundary:
    if direction=="right":
        for i in range(leftBoundary,rightBoundary+1):
            print(a[topBoundary][i],end=" ")
        direction="down"
        topBoundary+=1
    elif direction=="down":
        for i in range(topBoundary,bottomBoundary+1):
            print(a[i][rightBoundary],end=" ")
        direction="left"
        rightBoundary-=1
    elif direction=="left":
        for i in range(rightBoundary,leftBoundary-1,-1):
            print(a[bottomBoundary][i],end=" ")
        direction="up"
        bottomBoundary-=1
    else:
        for i in range(bottomBoundary,topBoundary-1,-1):
            print(a[i][leftBoundary],end=" ")
        direction="right"
        leftBoundary+=1
