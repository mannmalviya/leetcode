"""
LeetCode Problem: 49. Group Anagrams
Link:
- https://leetcode.com/problems/group-anagrams/description/
- https://neetcode.io/problems/anagram-groups/question?list=neetcode150

Date Solved: 26th November, 2025

Thought Process: 
- My very first thought was to compare every string with every other string and check if they are Anagrams of each other (using the isAnagram function implemented in prblm 242) and store them in a list if they are.
- But then I thought of using a hashmap! All anagrams can be identified by a dictionary that holds a count of each char in the str. I thought of using this dict as the key in the hashmap(so basically a dict with keys that are dicts). Turns out python doesn't let you do that,"dictionary keys must be immutable (unchangeable), and dictionaries are mutable".
- So since strings can be keys in a python dict, every str sorted shoud be the key(as all anagrams have the same sorted str)

Notes:
- 4th Problem in Neetcode150 under: Arrays & Hashing

"""

from typing import List

class Solution():
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
            The key idea here is the same as the sorting soln(implemented in `sorted_strs_as_keys`) or rather the idea I had in my incorrect soln. of using the dictionay of character counts as the key instead we should use a tuple! of 26 entries each corresponding to the number of times a particular letter occurs and use this tuple as the key of our hashmap!

            If there are m strings and the max len of string is n,

            Time Complexity: O(m*n)
            Space Complexity: O(m*n)
        """
        
        map = {}

        for s in strs:
            if self.count_chars(s) in map:
                map[self.count_chars(s)].append(s)
            else:
                map[self.count_chars(s)] = [s]

        l = []
        for key in map:
            l.append(map[key])

        return l

    def count_chars(self, s: str) -> tuple:
        l = [0]*26

        for c in s:
            l[ord(c) - 97] += 1
        
        return tuple(l)

    #-------------------------------------------------------------------

    def groupAnagrams_Inefficient(self, strs: List[str]) -> List[List[str]]:
        """
            I iterate over all strings in strs, I check if the str is an angram with any of the keys in the hashmap(using isAnagram(..) with timecomplex of O(n)), if it is not then I create a new key with the str and the value as a list with the str in it. Once you iterate over all strings, all anagrams are grouped.

            This soln. got Time limit exceeded on the 128th(passed 127/128) test case on leetcode. 
        
            If m is the number of strs in `strs` and n is the max len of a str. Then,

            Time Complexity: O(m*m*n)
            Space Complexity: O(m)
        """
        map = {}

        for str in strs:
            new = 1
            for key in map:
                if self.isAnagram(str, key):
                    map[key].append(str)
                    new = 0
                    break
            if new == 1:
                map[str] = [str]

        l = []
        for key in map:
            l.append(map[key])

        return l
    
    def isAnagram(self, str1:str, str2:str) -> bool:
        """
            Taken from problem 242. Valid Anagram

            Time Complexity: O(n) or O(1)
            Space Complexity: O(1)
        """
        if len(str1) != len(str2):
            return False
        
        count_dict1 = {}
        count_dict2 = {}

        for i in range(len(str1)):
            count_dict1[str1[i]] = 1 + count_dict1.get(str1[i], 0)
            count_dict2[str2[i]] = 1 + count_dict2.get(str2[i], 0)

        return count_dict1 == count_dict2

    #-------------------------------------------------------------------

    def sorted_strs_as_keys(self, strs: List[str]) -> List[List[str]]:
        """
            Create a hash map where each key is the sorted version of a string, and the value is a list of strings belonging to that anagram group.
        
            m be the number of strings and n the length of the longest string
         
            Time Complexity: O(m*nlogn) (it takes nlogn time to sort a str of len n & there are m strs in `strs`)
            Space Complexity: O(m*n) (its m*n because we need to account the space taken by the len n str in the key of the map and there are m strings in total so each of the m srings will have (max) n len str as its key)
        """
        
        map = {}
        grp_ana = []

        for str in strs:
            map["".join(sorted(str))] = []

        for str in strs:
            map["".join(sorted(str))].append(str)

        for key in map:
            l = map[key]
            grp_ana.append(l)

        return grp_ana

"""
    Incorrect soln. that uses a dict as the key in the main dict(hashmap). 

    def count_chars(self, str: str) -> dict:
        count = {}

        for c in str:
            count[c] = 1 + count.get(c, 0)

        return count
    
    def my_og_soln(self, strs: List[str]) -> List[List[str]]:
        map = {}
        grp_ana = []

        for str in strs:
            key = self.count_chars(str)
            map[key] = []

        for str in strs:
            key = self.count_chars(str)
            map[key].append(str)

        for key in map:
            l = map[key]
            grp_ana.append(l)

        return l
"""

def main():
    ans = Solution()

    #print(ans.count_chars("aabbbc"))

    print(ans.groupAnagrams(["cat","dog", "tac", "god","aaa"]))

    print(ans.groupAnagrams([""]))

    print(ans.isAnagram("str", "rts"))
    print(ans.isAnagram("sto", "rts"))

    return

if __name__ == "__main__":
    main()



