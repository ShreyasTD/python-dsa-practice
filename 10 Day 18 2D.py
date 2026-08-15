#1

matrix=[
         [1,2,3,4],
         [2,4,2,1],
         [2,3,4,2]
     ]

for row in matrix:
    for element in row:
        print(element,end=" ")
    print()

#printing by index
matrix=[[1,2,3],
         [2,4,1],
         [3,4,2]
     ]

for i in range(len(matrix)):
     for j in range(len(matrix[0])):
        print(matrix[i][j],end=" ")
     print()

#3
matrix=[[1,2,3],
         [2,4,1],
         [3,4,2]
     ]
total=0
for i in range(len(matrix)):
     for j in range(len(matrix[0])):
        print(matrix[i][j],end=" ")

     print()


#4. 2D integer list -> find sum of all elements
matrix=[[1,2,3],
         [2,4,1],
         [3,4,2]
     ]
total=0
for i in range(len(matrix)):
     for j in range(len(matrix[0])):
        total=matrix[[i][j]] # type: ignore
        print()

#5. create a function which returns maximum element of a 2d list passes as an argument.


#6 print sum of every row

matrix=[[1,2,3],[4,5,6],[7,8,9]]
total=0
for i in range(len(matrix)):
    rowSum=0
    for j in range(len(matrix[0])):
        rowSum+=matrix[i][j]
    print(rowSum) 

# 7. print sum of every column of a 2d list

matrix=[[1,2,3],[4,5,6],[7,8,9]]

total=0

for j in range(len(matrix[0])):

    colSum=0

    for i in range(len(matrix)):

        colSum+=matrix[i][j]

    print(colSum)

#8 .create a function which returns the number of even numbers in a 2d list.
def findEven(aList):
    evenCounter =0
    for row in aList:
        for ele in row :
            if ele%2==0:
                evenCounter+=1
    return evenCounter
print(findEven([[1,2,3],[3,7,8]]))

#9.find the main diagonal sum of a square matrix
a=[[1,2,3],[4,10,6],[7,8,9]]

total=0

order = 3

for i in range(len(a)):

    total+=a[i][order - (i + 1)]

print(total)

#10 
a=[[1,2,3],[4,10,6],[7,8,9]]

total=0

order = 3
for i in range(len(a)):
    for j in range(len(a[0])):
        if j==order -(i+1):
            total+=a[i][j]
print(total)