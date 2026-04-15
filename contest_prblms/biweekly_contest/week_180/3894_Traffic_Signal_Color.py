"""
LeetCode Problem: 3894. Traffic Signal Color
Link:
- https://leetcode.com/problems/traffic-signal-color/

Date Solved: April 11th, 2026
Total Time Spent: < 3mins

Thought Process:
- Didn't need to think

Notes:
- Bi-Weekly Contest Problem
- Could have solved this back in 5th grade :/
"""

class Solution:
    def trafficSignal(self, timer: int) -> str:
        """
            Time Complexity: O(1)
            Space Complexity: O(1)
        """
        if timer == 0:
            return "Green"
        elif timer == 30:
            return "Orange"
        elif (timer <= 90) and (timer > 30):
            return "Red"
        else:
            return "Invalid"
