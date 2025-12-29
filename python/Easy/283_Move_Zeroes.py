"""
LeetCode Problem: 283. Move Zeroes
Link:
- https://leetcode.com/problems/move-zeroes/description/

Date Solved: Dec 29th, 2025
Total Time Spent: -

Thought Process: 
- 

Notes:
- Random Easy problem
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]: # <<-- I changed return from None to List[int]
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        
            Time Complexity: O(n^2)
            Space Complexity: O(1)
        """

        i = 0
        num_zeros = 0

        while(i < len(nums)-num_zeros):
            if nums[i] == 0:
                k = i
                for j in range(i+1, len(nums)):
                    nums[k] = nums[j]
                    k = j
                nums[k] = 0
                num_zeros+=1
            else:
                i += 1

        return nums


def main():
    ans_obj = Solution()

    print(ans_obj.moveZeroes([1,0,0,2,0,3]))

    return

if __name__ == "__main__":
    main()
