"""
LeetCode Problem: 1877. Minimize Maximum Pair Sum in Array
Link:
- https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/?envType=daily-question&envId=2026-01-24

Date Solved: Jan 24th, 2025
Total Time Spent: 30mins + 15mins +15mins + 15mins

Thought Process: 
- I basically read the given Editorial solution and just implemented that, I don't even fully understand why this works:/

Notes:
- Daily Challenge problem
- saw hint 1 after 45mins (didn't help much as I already knew I needed to probably sort nums)
- saw hint 2 13 mins after hint 1 (didn't really make any light bulb go off)
- after spending 1hr15mins I looked at the soln
"""

from typing import List

class Solution:
    def minPairSum_initial(self, nums: List[int]) -> int:
        """
            - 
        
            Time Complexity: O(nlogn)
            Space Complexity: O(logn) (this is the space required for the sorting algorithm)
        """
        max_sum = 0

        for i in range(len(nums)//2):
            s = nums[i] + nums[len(nums)-i-1]
            if s > max_sum:
                max_sum = s

        return max_sum
