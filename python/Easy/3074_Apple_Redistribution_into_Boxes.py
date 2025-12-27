"""
LeetCode Problem: 3074. Apple Redistribution into Boxes
Link:
- https://leetcode.com/problems/apple-redistribution-into-boxes/description/

Date Solved: Dec 24th, 2025
Total Time Spent: Didn't track :/

Thought Process: 
- 

Notes:
- Daily Challenge problem
"""

from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        """
            - 
            
            Time Complexity: O(nlogn) where n is the length of capacity
            Space Complexity: O()
        """

        tot_apples = sum(apple)

        capacity.sort()
        
        space = 0
        for box in capacity[::-1]:
            continue
        
        return
    

def main():
    return

if __name__ == "__main__":
    main()