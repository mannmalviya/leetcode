"""
LeetCode Problem: 11. Container With Most Water
Link:
- http://neetcode.io/problems/max-water-container/question?list=neetcode150
- https://leetcode.com/problems/container-with-most-water/description/

Date Solved: 21st December, 2025
Total Time Spent: 50mins+45mins

Thought Process: 
- See below function comments

Notes:
- NeetCode150 problem 4 under Two Pointers
"""

from typing import List

class Solution():
    def maxArea(self, height: List[int]) -> int:
        """
            - Basically had to read all NeetCode hints to be able to do this one
            - We implement the 2 pointer solution, where we maintain one pointer at the start of the inp list `height` and one at the end, we reduce only the pointer which has a lower height as only the lower height out of the two line heights actually contributes to the total area of water contained.
        
            Time Complexity: O(n)
            Space Complexity: O(1)
        """ 
        def amt_water(h1, i1, h2, i2):
            """
                function to calculate the amount of water when we fix two heights
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

        p1 = 0
        p2 = len(height) - 1

        while(p1 < p2):
            area = amt_water(height[p1], p1, height[p2], p2)
            if area > max_area:
                max_area = area
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 +=1

        return max_area
    
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
                function to calculate the amount of water when we fix two heights
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
                function to calculate the amount of water when we fix two heights
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

    print(ans_obj.maxArea([1,8,6,2,5,4,8,3,7]))

    return

if __name__ == "__main__":
    main()