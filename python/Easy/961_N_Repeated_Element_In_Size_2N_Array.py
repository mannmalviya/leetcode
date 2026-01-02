"""
LeetCode Problem: 961. N-Repeated Element in Size 2N Array
Link:
- https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/?envType=daily-question&envId=2026-01-02

Date Solved: Jan 1st, 2026
Total Time Spent: <10mins on initial accepted soln

Thought Process: 
- Look at function comments below

Notes:
- Daily Challenge problem
"""

from typing import List

class Solution():
    def repeatedNTimes(self, nums: List[int]) -> int:
        """
            - This was the second solution I came up with, which is more efficient than the previous hashmap implementation
            - This soln actually uses the information given in the problem, that nums has 2*n elements and n+1 unique elements, this means that half the numbers in nums are the same and the other half are all unique numbers
            - Which means any number that appears more than once is the number that appears n times and is hence our answer

            Time Complexity: O(n)
            Space Complexity: O(n)
        """

        seen = set()

        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)

        return

    def repeatedNTimes_initial(self, nums: List[int]) -> int:
        """
            - Solving using a hashmap where the keys are every unique number in `nums` and the value is that numbers frequence
            - Then traverse the hash map and return the number that has a frequency = n
            - The hash map can be created in linear time and the hashmap can be searched for a number that appears n times in linear time as well!

            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        freq_map = {}

        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)

        n = len(nums) / 2
        for num in freq_map:
            if freq_map[num] == n:
                return num 

        return



def main():
    return

if __name__ == "__main__":
    main()