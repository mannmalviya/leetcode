"""
LeetCode Problem: 3805. Count Caesar Cipher Paris
Link:
- https://leetcode.com/problems/count-caesar-cipher-pairs/description/

Date Solved: Jan 10th, 2026
Total Time Spent: 

Thought Process: 
- Although I was able to come up with the brute force solution with a lot of difficulty during the contest it was O(n^3) time comp. and hence timedout on the last few of the stress test cases

Notes:
- Weekly Contest Problem
"""

from typing import List

class Solution:
    def countPairs_Initial(self, words: List[str]) -> int:
        """
            - I worte a helper function `similar(..)` that given two strings can determine whether one of the two strings is a caesar cipher of the other in O(n) time where n is the length of the strings (its given in the problem that all strings in the list `words` are of the same length)
            - Once I have the function to compare two strings I just need to compare all of the pairs of strings in `words` with each other, which takes O(n^2) time
            - This solution DOES NOT PASS the leetcode tests, I spent almost all my contest time on this almost 1hr15mins:/

            Time Complexity: O(n^3)
            Space Complexity: O(1)
        """

        def similar(s1:str ,s2: str) -> bool:
            if ord(s1[0]) < ord(s2[0]):
                tmp = s1
                s1 = s2
                s2 = tmp
            
            diff = ord(s1[0]) - ord(s2[0])
            
            for i in range(1, len(s2)):
                c2 = s2[i]
                c2 = chr(((ord(c2)-ord('a') + diff) % 26) + ord('a'))            
                if c2 != s1[i]:
                    return False

            return True

        ans = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if similar(words[i], words[j]):
                    ans += 1
        return ans
        
    def countPairs(self, words: List[str]) -> int:
        """
        
            Time Complexity: O()
            Space Complexity: O()
        """
        
        return