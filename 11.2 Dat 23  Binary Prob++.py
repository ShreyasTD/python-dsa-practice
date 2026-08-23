#Given a sorted list and target, return the indices of two numbers whose num is target
#ind the maximum subarray sum of length k
#rotate a 2D list by 90 deg clockwise. 

def rotate_in_place(matrix):
    n = len(matrix)
    
    # Step 1: Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
