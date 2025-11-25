"""
LeetCode Problem: 242. Valid Anagram
Link:
- https://leetcode.com/problems/valid-anagram/description/
- https://neetcode.io/problems/is-anagram/question?list=neetcode150
Date Solved: November 24th, 2025 (resolved)

Thought Process: 
- see below

Notes:
- Resolved this.
- 2nd Neetcode150 prblm
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            This is a simple soln. using a hash map(dictionary in python). Build a dict. for both inp strings, where the key is each character and the value is the number of times it has occured. If the two dictionaries are the same then the strings are anagrams of each other.
        
            Time Complexity: O(n)
            Space Complexity: O(1) (because we can only have at most 26 char keys in the hash as there are only 26 characters)
        """
        if len(s) != len(t):
            return False

        dict_s = {}
        dict_t = {}

        for i in range(len(s)):        
            dict_s[s[i]] = 1 + dict_s.get(s[i], 0) # .get() gets the value associated with key, if dne defaults to 0
            dict_t[t[i]] = 1 + dict_t.get(t[i], 0)

        if dict_s == dict_t:
            return True

        return False

    def sorting_sol(self, s: str, t: str) -> bool:
        """
            This is a short soln. exploiting the built in sorted(..) function.

            Time Complexity: O(nlogn) (.sorted(..) has time comp. of O(nlogn), uses Timsort algorithm)
            Space Complexity: O(n) (.sorted(..) has space comp. of O(n) because it creates a new list)
        """
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
    
    def my_og_soln(self, s: str, t: str) -> bool:
        """
            This was my original soln., the one in isAnagram(...) is a cleaner version taken basically from the official soln on neetcode.
            
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        if len(s) != len(t):
            return False

        d1 = {}
        d2 = {}

        for c in s:
            if c in d1:
                d1[c] += 1
            else:
                d1[c] = 1

        for c in t:
          if c in d2:
              d2[c] += 1
          else:
              d2[c] = 1
  
        if d1 == d2:
            return True

        return False


def main():
    ans = solution()

    print(ans.isAnagram("god", "ddg"))

    return

if __name__ == "__main__":
    main()