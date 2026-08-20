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