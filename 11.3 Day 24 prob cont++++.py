"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""

def maxProfit(a):
    minPrice = 10 ** 10
    maxP=0


    for i in range(len(a)):
        minPrice = min(minPrice, a[i])
        maxP = max(maxP, a[i]-minPrice)
    return maxP

#Check if a two strings given as a parameters of a function is valid anagram or not
s1="cat"

s2 = "act"



# valid anagram



s1="apple"

s2="plea"



# not valid anagram



# Don't go for O(n^2).
# hash map problem 


def isValidAnagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    freq={}
    for ele in s1:
        freq[ele] = freq.get(ele,0)+1
    for ele in s2:
        if ele not in freq:
            return False
        freq[ele]-=1


        if freq[ele]<0:
            return False
    return True
    


# -> take 2 maps (for s1,s2)
# compare every elemet's value in both s1 & s2
# at any point of comparison, if frequency of same character is different in both the maps , return False
# return True

#Merge two Sorted lists.
"""[1,2,3]

[0,5]



return [0,1,2,3,5]"""

# merge two sorted list


def mergeList(a,b):
    i=0
    j=0
    result = []
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            result.append(a[i])
            i+= 1
        else:
            result.append(b[j])
            j+= 1
    # cover the edge case
    while i<len(a):
        result.append(a[i])
        i+= 1
    while j<len(b):
        result.append(b[j])
        j+= 1
    return result

print(mergeList([1,2,3],[0,5]))

#Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping."""