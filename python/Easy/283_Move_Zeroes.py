"""
LeetCode Problem: 283. Move Zeroes
Link:
- https://leetcode.com/problems/move-zeroes/description/

Date Solved: Dec 29th, 2025
Total Time Spent: -

Thought Process: 
- see bellow function comments

Notes:
- Random Easy problem
- I also solved this problem in C++ on leetcode and the same algorithm implemented in C++ performed significantly better in runtime and memory compared to the python implementation.
"""

from typing import List

class Solution:
    def moveZeroes_naive(self, nums: List[int]) -> List[int]: # <<-- I changed return from None to List[int]
        """
        Do not return anything, modify nums in-place instead.
        """
        """
            - Traverse throught the input array nums, for every 0 enountered push all the elements after the zero by one posistion ahead and set the last element in the array to zero
            - This was the first solution I came up with
            
            Time Complexity: O(n^2)
            Space Complexity: O(1), does everything in place
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

    def moveZeroes_2pointers(self, nums: List[int]) -> List[int]:
        """
            - Taken from official Editorial Solution, this is the most optimal algorithm!
            - The problem can be thought of as shifiting all the non-zero elements to the front of the list while maintainig their order
            - Maintain 2 pointers, one that keeps track of the first non-zero element position and the other iterates throught the list looking for non-Zero elements
            - Whenever the 2nd ptr encounters a non-Zero Element it sets that index to zero and sets the element pointed to by the first pointer to the non-zero number
            - At the end of iterating over the entire list, all non-zero elements will be at the front in the same order of their occurence in nums
            - p1 is the lastNonZeroFountAt and p2 is the curr pointer
            
            Time Complexity: O(n)
            Space ComplexityL O(1), does everything in place
        """

        p1 = 0

        for p2 in range(len(nums)):
            if nums[p2] != 0:
                if p1 != p2:
                    nums[p1] = nums[p2]
                    nums[p2] = 0
                p1 += 1

        return nums


def main():
    ans_obj = Solution()

    print(ans_obj.moveZeroes_2pointers([1,0,1]))

    return

if __name__ == "__main__":
    main()
