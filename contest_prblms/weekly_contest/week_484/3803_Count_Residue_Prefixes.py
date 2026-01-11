"""
LeetCode Problem: 3803. Count Residue Prefixes
Link:
- https://leetcode.com/problems/count-residue-prefixes/description/

Date Solved: Jan 10th, 2026
Total Time Spent: <4mins for initial soln

Thought Process: 
- very straight forward python implementation for this problem below

Notes:
- Weekly Contest Problem
"""

class Solution:
    def residuePrefixes_initial(self, s: str) -> int:
        """
            - I build up the prefix with each iteration over s
            - I check check the number of distinct characters by converting the prefix into a set and checking the length of that set
            - Beats 18% in runtime and 28% in space
            - This was my implementation in the contest
            
            Time Complexity: O(n)
            Space Complexity: O(1) extra space
        """
        ans = 0
        prefix = ""

        for c in s:
            prefix += c
            if len(set(prefix)) == len(prefix) % 3:
                ans+=1

        return ans
    
    def residuePrefixes_second_imp(self, s:str) -> int:
        """
            - beats 100% in runitme and 75% in space

            Time and Space comp same as above
        """
        ans = 0
        unique_chrs = set()
        l = len(s)

        for i in range(l):
            if s[i] not in unique_chrs:
                unique_chrs.add(s[i])
            if len(unique_chrs) == (i+1) % 3:
                ans+=1
        
        return ans
        


