"""
LeetCode Problem: 1351. Count Negative Numbers in a Sorted Matrix
Link:
- https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/?envType=daily-question&envId=2025-12-28

Date Solved: Dec 27th, 2025
Total Time Spent: < 5 mins

Thought Process: 
- Easy question got it quickly and in the first attempt

Notes:
- Daily LeetCode Challenge
"""

from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
            - Utilize the fact that the inout 2D list is sorted in decreasing order.
            - So traverse the rows backwards and the numbers in a row backwards!

            Time Complexity: O(n^2)
            Space Complexity: O(1) extra space
        """
        
        count = 0

        for row in grid[::-1]:
            for num in row[::-1]:
                if num < 0:
                    count+=1
                else:
                    break
        return count

def main():
    return

if __name__ == "__main__":
    main()
