"""
LeetCode Problem: 3075. Maximize Happiness of Selected Children
Link:
- https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2025-12-25

Date Solved: Dec 24th, 2025
Total Time Spent: approx 20mins

Thought Process: 
- Look at function comments below
- Pretty easy question

Notes:
- Daily Challenge problem
"""

from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        """
            - In each of the k iterations pick the happiest kid
            - After picking a kid make sure to subtract 1 from the happiness of all other kids
            - Make sure to not decrement a kids happiness below 0
            - I sort the initial list so that I have the happiest kids one after the other available and I don't need to search for the happiest kid each iteration
            
            Time Complexity: O(nlogn) where len(happiness) = n
            Space Complexity: O(1)
        """

        happiness.sort() # O(nlogn)

        max_happy = 0

        for i in range(k):
            happy = happiness[len(happiness)-1-i] - i
            if happy > 0:
                max_happy += happy
        
        return max_happy

def main():
    return

if __name__ == "__main__":
    main()
