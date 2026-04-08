"""
LeetCode Problem: 3889. Mirror Frequency Distance
Link:
- https://leetcode.com/problems/mirror-frequency-distance/description/

Date Solved: April, 2026
Total Time Spent: 41 mins (2 incorrect attempts)

Thought Process:
- see below function comment 

Notes:
- Weekly Contest Problem
- This was the only problem I was able to solve in this contest
- I ended up solving this problem with some trial and error, that's why I got 2 incorrect attempts
- I was little confused by what is meant by unique characters in the string, does it mean a character that only occurs once or computing the difference for a particular character only a single time and not for all the instances it appears.
- I guess from the context of the problem it only makes sense to be the latter because with the first interpretation the freq of a unique character x would always be 1!

"""

class Solution:
    def mirrorFrequency_my_og_sol(self, s: str) -> int:
        """
            - I compute a dict that contains the freq of each char in s
            - Then for each unique char c I find it's mirror using `mirror(c)`
            - Then I computer |freq(c) - freq(mirror(c))| and add that to my running sum to return

            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        def mirror(s: str):
            """
                - Helper function that mirrors a character
                Time Complexity: O(1)
                Space Complexity: O(1)
            """
            if (ord(s) >= ord('a')) and (ord(s) <= ord('z')):
                # mirroring a letter
                return chr(ord('z') - ord(s) + ord('a'))
            else:
                # mirroring a digit
                return chr(ord('9') - ord(s) + ord('0'))
    
        # a dict of freqs of all distinct chars in s
        fmap = {}
        for c in s:
            if c in fmap:
                fmap[c] += 1
            else:
                fmap[c] = 1
        
        sum = 0
        for char in fmap: # for each unique char in the map
            if mirror(char) in fmap:
                mf = fmap[mirror(char)]
            else:
                mf = 0
            sum += abs( fmap[char] - mf )
        
        return sum
