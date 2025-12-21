"""
LeetCode Problem: 11. Container With Most Water
Link:
- http://neetcode.io/problems/max-water-container/question?list=neetcode150
- https://leetcode.com/problems/container-with-most-water/description/

Date Solved: 20th December, 2025
Total Time Spent: 50mins+

Thought Process: 
-

Notes:
- Spent days on this question, my brain just cannot understand it. Defeated I shall take a break from it and come back to it at a later time! - 20th Dec 2025
"""

from typing import List

class Solution():
    def maxArea(self, height: List[int]) -> int:
        """
        
            Time Complexity: O()
            Space Complexity: O()
        """
        pass
    
    def BruteForce(self, height: List[int]) -> int:
        """
            - For all pairs of lines calculate the amount of water the container can store, in the end return the max area of water any of the pairs of lines was able to save.
            - Doesn't pass LeetCode, with 'MEMORY LIMIT EXCEEDED' error!
            
            If there are n input lines, i.e., len(height) = n

            Time Complexity: O(n^2)
            Space Complexity: O(n^2)
        """
        def amt_water(h1, i1, h2, i2):
            """
            """
            if i1 > i2:
                b = i1 - i2
            else:
                b = i2 - i1
            
            if h1 > h2:
                h = h2
            else:
                h = h1

            return b*h
        
        areas = []

        for i in range(len(height)):
            for j in range(i+1, len(height)):
                areas.append(amt_water(height[i], i, height[j], j))

        return max(areas)

    def BruteForce2(self, height: List[int]) -> int:
        """
            - Was able to optimze the memory use by not storing the areas for each pair of lines and instead just maintaining the max. area seen so far.
            - Still doesn't pass! Fails with 'TIME LIMIT EXCEEDED' error!

            Time Complexity: O(n^2)
            Space Complexity: O(1)
        """
        def amt_water(h1, i1, h2, i2):
            """
            """
            if i1 > i2:
                b = i1 - i2
            else:
                b = i2 - i1
            
            if h1 > h2:
                h = h2
            else:
                h = h1

            return b*h
        
        max_area = 0

        for i in range(len(height)):
            for j in range(i+1, len(height)):
                if max_area < amt_water(height[i], i, height[j], j):
                    max_area = amt_water(height[i], i, height[j], j)

        return max_area


def main():
    ans_obj = Solution()

    print(ans_obj.BruteForce([1,8,6,2,5,4,8,3,7]))

    return

if __name__ == "__main__":
    main()