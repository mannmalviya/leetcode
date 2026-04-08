"""
LeetCode Problem: 704. Binary Search
Link:
- https://leetcode.com/problems/binary-search/

Date Solved: Feb 25th, 2026
Total Time Spent: <12mins

Thought Process: 
- Straight forward problem, just need to directly apply Binary Search
- So the question is really just testing whether you know Binary Search and how to implement it

Notes:
- NeetCode150: Under Binary Search
"""

from typing import List

class Solution:
    def search_iterative(self, nums: List[int], target: int) -> int:
        """
            - Binary Search algorithm implementation using loops

            Time Complexity: O(log(n))
            Space Complexity: O(1)
        """

        upper = len(nums)
        lower = 0

        while (upper >= lower):
            index = (upper + lower) // 2
            if target == nums[index]:
                return index
            elif target > nums[index]:
                lower = index + 1
            else:
                upper = index - 1

        return -1
    
    def search_recursive(self, nums: List[int], target: int) -> int:
        """
            - Binary Search algorithm implementation using recursion
        
            Time Complexity: O()
            Space Complexity: O()
        """

        #TODO

        return
