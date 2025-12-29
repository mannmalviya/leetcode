"""
LeetCode Problem: 1480. Running Sum of 1d Array
Link:
- https://leetcode.com/problems/running-sum-of-1d-array/description/

Date Solved: Dec 28th, 2025
Total Time Spent: 1min 10s

Thought Process: 
- This question is so easy bruh
- There MUST be a one line for this

Notes:
- Random easy problem
"""

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
            - Iterate through the list while maintaining the sum of all elements seen so far, this is your running sum
            - Append the running sum to your output list every iteration
        
            Time Complexity: O(n), where len(nums) = n
            Space Complexity: O(n) for output, O(1) extra space
        """
        run_sum = []
        sum = 0
        for num in nums:
            sum+=num
            run_sum.append(sum)

        return run_sum
    