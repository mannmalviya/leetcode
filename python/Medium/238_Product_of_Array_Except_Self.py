"""
LeetCode Problem: 238. Product of Array Except Self
Link:
- https://leetcode.com/problems/product-of-array-except-self/description/
- https://neetcode.io/problems/products-of-array-discluding-self/question?list=neetcode150

Date Solved: 14th December, 2025

Thought Process: 
- I was simply unable to solve this problem, all the solutions I could think of were O(n^2) time complexity.
- I looked at hint 1 on Leetcode (which actually happened to be hint3 on neetcode:/) which gave away the main idea of maintaining a prefix and sufix products to avoid recomputation. Once I understood this hint I was very quickly able to write the pseudo code and then the actual solution which passes.

Notes:
- 7th NeetCode Problem
"""

from typing import List

class Solution:
    def productExceptSelf_optimal(self, nums: List[int]) -> List[int]:
        """
            
            Time Complexity: O(n)
            Space Complexity: O(1)
        """


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            This was my first implementation of the O(n) solution, after reading the hint that, we need to maintain a prefix and sufix array to avoid recomputing values.
        
            Time Complexity: O(n)
            Space Complexity: O(n)
        """

        # Compute Prefix array, O(n)
        pre = {}
        
        for i in range(len(nums)):
            if i == 0:
                pre[i] = 1
            else:
                pre[i] = pre[i-1] * nums[i-1]
        
        # Computer Sufix array, O(n)
        suf = {}

        for i in range(len(nums)-1 , -1, -1):
            if i == len(nums) - 1:
                suf[i] = 1
            else:
                suf[i] = suf[i+1] * nums[i+1]

        # Computer the answer, O(n)
        answer = []

        for i in range(len(nums)):
            answer.append(pre[i] * suf[i])

        return answer
    
    def Brute_Force(self, nums: List[int]) -> List[int]:
        """
            This is one of the ways to do the brute force solution. I was able to think of a few more ways to do O(n^2) soln. lol.
        
            Time Complexity: O(n^2)
            Space Complexity: O(1) extra space, O(n) space for the output
        """        
        answer = []

        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i != j:
                    prod = prod * nums[j]
            answer.append(prod)

        return answer

    def division(self, nums: List[int]) -> List[int]:
        """
            Using division
        
            Time Complexity: O()
            Space Complexity: O()
        """




        return

def main():

    nums = [1,2,3]

    ans_obj = Solution()

    print(ans_obj.productExceptSelf(nums))

    return

if __name__ == "__main__":
    main()