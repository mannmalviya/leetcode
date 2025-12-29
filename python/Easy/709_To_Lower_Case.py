
"""
LeetCode Problem: 709. To Lower Case
Link:
- https://leetcode.com/problems/to-lower-case/

Date Solved: Dec 28th, 2025
Total Time Spent: <1min

Thought Process: 
- This question is so easy bruh

Notes:
- Random easy problem
"""

class Solution:
    def toLowerCase(self, s:str) -> str:
        """
            - This implementation doesn't use any ready made helper functions
            - add every character to result str, if it's upper case
                      - Performace same as using .lower()
        
            Time Complexity: O(n)
            Space Complexity: O(n) for output string
        """

        result = ""

        for c in s:
            if ord(c) >= ord('A') and ord(c) <= ord('Z'):
                result += chr(ord(c) + 32)
            else:
                result += c

        return result

    def toLowerCase_1liner(self, s: str) -> str:
        """
            - Using prebuilt helper function .lower() this question is a joke

            Time Complexity: O(n)
            Space Complexity: O(n) for output lowercased string
        """
        return s.lower()
    



