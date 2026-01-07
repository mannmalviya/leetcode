"""
LeetCode Problem: 42. Trapping Rain Water
Link:
- https://leetcode.com/problems/trapping-rain-water/submissions/1877120100/
- https://neetcode.io/problems/trapping-rain-water/question?list=neetcode150

Date Solved: Jan 2nd, 2026
Total Time Spent: 2.5hrs + 1.5 = 4hrs total for just solving it for the first time!

Thought Process: 
- Look at function comments below

Notes:
- NeetCode 150, 5th question under Two Pointers
- No hints used, all me
- This is basically my second hard problem that I have solved. Humble beginnings...
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
            - 

            Time Complexity: O(n^2)
            Space Complexity: O(1) extra space
        """

        total_trap_water = 0
        i = 0
        while(i < len(height)-1):
            j = i+1
            while(j < len(height) and height[j] < height[i]):            
                j += 1
            if j == len(height):
                print(height[i:len(height)][::-1])
                amt_water = self.trap(height[i:len(height)][::-1])
                return total_trap_water + amt_water    
            width = j - i - 1
            total_trap_water += width * height[i]
            for k in range(i+1, j):
                total_trap_water -= height[k]
            i = j
        
        return total_trap_water

    
def main():
    ans_obj = Solution()

    print(ans_obj.trap([4,2,0,3,2,5]))

    return

if __name__ == "__main__":
    main()