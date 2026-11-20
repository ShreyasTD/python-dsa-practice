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


# find the maximum subarry of the list
def max_subarray(nums):
    current_sum = max_sum = nums[0]
    for x in nums[1:]:
        current_sum = max(x, current_sum + x)
        max_sum = max(max_sum, current_sum)
    return max_sum


print([-2, 1, -3, 4, -1, 2, 1, -5, 4])
