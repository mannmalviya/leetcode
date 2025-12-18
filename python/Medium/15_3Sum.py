"""
LeetCode Problem: 15. 3Sum
Link:
- https://leetcode.com/problems/3sum/description/
- https://neetcode.io/problems/three-integer-sum/question?list=neetcode150

Date Solved: 

Thought Process: 
-

Notes:
-
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        
            Time Complexity: O()
            Space Complexity: O()
        """
        def twosum(nums: List[int], target: int):

            map = {}

            for i, num in enumerate(nums):
                if num not in map:
                    map[num] = i
                if (target-num) in map:
                    print(f"target={target}= {num} + {target-num}")
                    return i, map[target-num] 

            return -1, -1

        ans = []

        for c in range(len(nums)):
            i,j = twosum(nums[c+1:], -1*nums[c])
            if (i != -1) and (j != -1):
                ans.append([nums[c], nums[i+c+1], nums[j+c+1]])

        unique = [list(t) for t in {tuple(sorted(lst)) for lst in ans}]

        return unique



    def Brute_Force(self, nums: List[int]) -> List[List[int]]:
        """
            - Try every possible triplet of numbers from num and check if they add upto 0, if yes then append a list of the triplet into the answer list to be returned.
                
            Time Complexity: O(n^3)
            Space Complexity: O(1) extra space, O(n) for storing the output
        """

        ans = []

        if len(nums) < 3:
            return []

        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        ans.append([nums[i], nums[j], nums[k]])
                        
        return ans


def main():

    ans_obj = Solution()

    print(ans_obj.threeSum([-1, 0, 1, 2, -1, -4]))

    return

if __name__ == "__main__": main()