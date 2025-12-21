"""
LeetCode Problem: 15. 3Sum
Link:
- https://leetcode.com/problems/3sum/description/
- https://neetcode.io/problems/three-integer-sum/question?list=neetcode150

Date Solved: 
Total Time Spent: 

Thought Process: 
-

Notes:
- Spent days on this question, my brain just cannot understand it. Defeated I shall take a break from it and come back to it at a later time! - 20th Dec 2025
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        
            Time Complexity: O()
            Space Complexity: O()
        """

        # TODO

        return

    def threeSum_HashMap(self, nums: List[int]) -> List[List[int]]:
        """
        
            Time Complexity: O()
            Space Complexity: O()
        """

        # TODO

        return

    def Brute_Force(self, nums: List[int]) -> List[List[int]]:
        """
            - Try every possible triplet of numbers from num and check if they add upto 0, if yes then append a list of the triplet into the answer list to be returned.
            - Also nums is sorted at the very starts so that in the end we can remove duplicate triplets easily    
            
            Time Complexity: O(n^3)
            Space Complexity: O(m) where m is the number of triplets
        """

        # sorting it so that we can return only the unique triplets that add to 0
        # sorting makes it straightforward to remove the duplicate triplets
        nums.sort() # O(nlogn)

        # trying every possible subset of size 3 to have a sum of 0
        ans = []
        
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        ans.append((nums[i], nums[j], nums[k]))

        return [list(a) for a in set(ans)]


def main():

    ans_obj = Solution()

    print(ans_obj.threeSum_HashMap([-1, 0, 1, 2, -1, -4]))

    return

if __name__ == "__main__": main()