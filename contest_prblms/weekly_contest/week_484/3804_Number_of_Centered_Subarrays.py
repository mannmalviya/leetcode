"""
LeetCode Problem: 3804. Number of Centered Subarrays
Link:
- https://leetcode.com/problems/number-of-centered-subarrays/description/

Date Solved: Jan 10th, 2026
Total Time Spent: <15mins

Thought Process: 
- very straight forward python implementation for this problem below
- LeetCode suprisingly accepted the brute force solution

Notes:
- Weekly Contest Problem
"""

from typing import List

class Solution:
    def centeredSubarrays_initial(self, nums: List[int]) -> int:
        """
            - This is basically a brute force soln. that I implemented in the contest
            - I generate all possible subarrays using 2ptrs i & j marking the start and end of all subarrays
            - while maintaining a running sum for each subarray
            - I then check if the subarray sum is present as an element in the set of elements of the subarray
            - beats 12% in runtme and 57% in memory

            Time Complexity: O(n^2)
            Space Complexity: O(1)        
        """
        
        ans = len(nums)

        for i in range(len(nums)-1):
            sum = nums[i]
            for j in range(i+1, len(nums)):
                s = set(nums[i:j+1])
                sum += nums[j]
                if sum in s:
                    ans+=1
        return ans

    def centeredSubarrays_second(self, nums: List[int]) -> int:
        """
            - same as above just made small optimizations to imporve the beats :p
            - beats 74% in runtime and 57% in memory
        
            same Time and Space comp.
        """
        ans = len(nums)

        n = len(nums)

        for i in range(n-1):
            sum = nums[i]
            eles = {nums[i]}
            for j in range(i+1, n):
                sum += nums[j]
                eles.add(nums[j])
                if sum in eles:
                    ans+=1
        return ans
