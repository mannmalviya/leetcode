"""
LeetCode Problem: 1975. Maximum Matrix Sum
Link:
- https://leetcode.com/problems/maximum-matrix-sum/description/?envType=daily-question&envId=2026-01-05

Date Solved: Jan 5th, 2026
Total Time Spent: idk, took longer than it should have! (probably more than an hour, but less than 2hrs?)

Thought Process: 
- I initially thought there will be a clever way to apply the operation to the matrix so as to maximize the sum by making the smallest possible numbers negative and then finally compute the sum of the transformed matrix. I simply wasn't able to think up an algorithm that makes the smallest numbers negative in both the rows and columns. 
- The hints basically gave the solution away.
- It is possible to reduce the number of negative numbers in a row/column to either 0 or 1, if theres an even number of negative numbers then you can make the entire thing positive and if theres an odd number of ones then you can reduce it to one negative number in the row/column.
- So if theres an even number of -ve nums in a row/col you can make the entire thing positive and if theres an odd number of -ve nums then you make the smallest number in the row/col the -ve number.
- So if you first apply the operation to only the rows, you can make one element in that row -ve, then you can go column by column doing the same thing, so essentially you end up with only one negative number in the matrix and you make the smallest number in the matrix negative, but thats only if there's an odd number of negative numbers in the matrix.

Notes:
- Daily Challenge problem
- I ended up looking at both the problem hints given, 
    hint1: try to use the operation so that each row has only one negative number.
    hint2: If you only have one negative element you cannot convert it to positive.
- My algorithm and implementation are basically identical to the official leetcode editorial solution given!
- I was also late in submitting it and had to redeem a makeup ticket, I think I get a total of 3 makeup tickets per month, so I have 2 left for the rest of the month.
"""

from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        """
            - Count up the number of negative numbers in the matrix
            - If there's an even number of negative numbers then just return the sum of all numbers in the matrix(taking the absolute value of the negative numbers), beacuse you will be able to transform the matrix into all positive numbers.
            - If there's an odd number of negative numbers then make the smallest number(ny absoute value) in the matrix negative, and then return the sum of the matrix(I implemented this in a clever way by subtracting the smallest number from the absolute values sum of all elements of the matrix)
            - While calculating the absolute sum, I also track the smallest absolute value
            
            len(matrix) = n
            Time Complexity: O(n)
            Space Complexity: O(1) extra space
        """
        
        if matrix == [[]]:
            return 0

        num_neg = 0
        matrix_sum = 0
        smallest = abs(matrix[0][0])

        for row in matrix:
            for n in row:
                matrix_sum += abs(n)
                if abs(n) < smallest:
                    smallest = abs(n)
                if n < 0:
                    num_neg+=1
        
        if num_neg%2 == 0:
            return matrix_sum
        else:
            return matrix_sum - smallest - smallest
