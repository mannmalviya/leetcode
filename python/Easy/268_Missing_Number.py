"""
LeetCode Problem: 268. Missing Number
Link:
- https://leetcode.com/problems/missing-number/?envType=problem-list-v2&envId=mw87u3z5

Date Solved: April 8th, 2026
Total Time Spent: <15mins (on initial sol)

Thought Process:
- see below function comment

Notes:
- So many ways of solving such a simple problem
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
            - I make a new list, `ns`, of size n+1 (including an extra space for the missing number) initialized to all 0s, then I traverse through `nums` since we have numbers in range [0,n] I mark the index of seen numbers as 1. Then after going through all the numbers in `nums` I check which index still has a 0, thats the missing number! 
            - This was my own soln
            
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        n = len(nums)

        ns = [0] * (n+1)

        for num in nums:
            ns[num] = 1

        for i in range(n+1):
            if ns[i] == 0:
                return i

    def missingNumber_XOR_approach(self, nums: List[int]) -> int:
        """
            - If you xor a number with 0 -> it remains same
            - If you xor a number with itself -> it become 0
            - If you xor 2 different numbers -> its still the xor of the 2 numbers
            - First we will xor all the numbers in nums together and then xor that with numbers in range [0,n], all the same numbers will cancel out (because of the 2nd property mentioned above about xor) and the only number remaining will be the missing number
            
            Time Complexity: O(n)
            Space Complexity: O(1)
        """

        n = len(nums)

        xor_all = 0
        for num in nums:
            xor_all ^= num

        for i in range(n + 1):
            xor_all ^= i

        return xor_all
    
    def missingNumber_sum_approach(self, nums: List[int]) -> int:
        """
            - Since we need all the numbers in the range [0,n]
            - We can find the missing number by subtracting the sum of numbers in `nums` with n(n+1)/2 and that difference will give you the missing number!

            Time Complexity: O(N)
            Space Complexity: O(1)

        """
        n = len(nums)

        sum = n * (n+1) // 2

        nums_sum = 0
        for num in nums:
            nums_sum += num

        return sum - nums_sum
    
    def missingNumber_sorting_approach(self, nums: List[int]) -> int:
        """
            - lol just sort th list and then match the index of each element to the value at that index, if they dont match that index is the missing number.
            - again its cuz the numbers are in range [0,1]

            Time Complexity: O(nlogn)
            Space Complexity: O(1)
        """

        nums.sort()

        for i in range(len(nums)):
            if i != nums[i]:
                return i

        return len(nums)
    