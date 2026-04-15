"""
LeetCode Problem: 3898. Find the Degree of Each Vertex
Link:
- https://leetcode.com/problems/find-the-degree-of-each-vertex/

Date Solved: April 11th, 2026
Total Time Spent: 10 mins

Thought Process:
- see below function comments

Notes:
- Weekly Contest Problem
"""

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        """
            - 
        
            Time Complexity: O()
            Space Complexity: O()
        """
        ans = []

        for row in matrix:
            degree = 0
            for i in row:
                if i == 1:
                    degree+=1
            ans.append(degree)
        return ans
