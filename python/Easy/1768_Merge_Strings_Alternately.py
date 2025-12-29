"""
LeetCode Problem: 1768. Merge Strings Alternately
Link:
- https://leetcode.com/problems/merge-strings-alternately/description/

Date Solved: Dec 28th, 2025
Total Time Spent: -

Thought Process: 
- Easy question, it's embarrassing that it took me so long to get;(

Notes:
- Random problem
"""

class Solution:
    def mergeAlternately_initial(self, word1: str, word2: str) -> str:
        """
            - Iterate over the strings simultaneously, so essentially uses only one pointer
            - First append the letter from string 1 then letter from string 2
            - If one of the strings is over, then only append letters from the other string
            - This was my initial solution that I came up with
            
            Time Complexity: O(m+n), where len(word1) = m and len(word2) = n
            Space Complexity: O(1) extra space
        """
        if len(word1) >= len(word2):
            l = len(word1)
        else:
            l = len(word2)
        
        merged = ""
        for i in range(l):
            if i >= len(word1):
                merged += word2[i]
            elif i >= len(word2):
                merged += word1[i] 
            else:
                merged += word1[i] + word2[i]

        return merged
    

    def mergeAlternately_1pointer(self, word1: str, word2: str) -> str:
        """
            - After reading the official leetcode solution editorial
            - I found out I could clean up my intial solution by using max(,) and
            - I can also make the logic in the loop more simple
            - Even though comlexity remains the same as my initial solution, it beat more people in the runtime and memory usage!

            Time Complexity: O(m+n), where len(word1) = m and len(word2) = n
            Space Complexity: O(1) extra space
        """
        l = max(len(word1), len(word2))

        merged = ""
        for i in range(l):
            if i < len(word1):
                merged += word1[i]
            elif i < len(word2):
                merged += word2[i] 

        return merged
        
    def mergeAlternately_2pointer(self, word1: str, word2: str) -> str:
        """
            - Basically just implementing the solution given in the official leetcode editorial solution 
            - This prblm can also be done by maintaining 2 seperate pointers to iterate over each of the input strings
            
            Time Complexity: O(m+n)
            Space Complexity: O(1) extra space
        """

        merged = ""

        i = 0
        j = 0
        
        while (i<len(word1) or j<len(word2)):
            if i<len(word1):
                merged += word1[i]
            if j<len(word2):
                merged += word2[j]
            
            i+=1
            j+=1

        return merged