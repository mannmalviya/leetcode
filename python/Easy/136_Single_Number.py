"""
LeetCode Problem: 136. Single Number
Link:
- https://leetcode.com/problems/single-number/

Date Solved: April 10th, 2026
Total Time Spent: <1 mins 

Thought Process:
- see below function comment

Notes:
- I already knew the trick from a previous problem I solved 
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
            - When you xor two same numbers together you get 0
            - When you xor a number with 0 you get the same number
            - So if you xor all numbers together, the duplicates in nums will cancel each other and only the one number that doesn't have a duplicate will remain.

            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        xor = 0

        for num in nums:
            xor ^= num

        return xor
    