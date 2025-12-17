"""
LeetCode Problem:
Link:
- https://leetcode.com/problems/valid-palindrome/description/
- https://neetcode.io/problems/is-palindrome/question?list=neetcode150

Date Solved: 15th December, 2025

Thought Process: 
- See function comments

Notes:
- First problem under Two Pointers in NeetCode150
- 1st problem of NeetCode150 under: Two Pointers
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
            - This was my initial implementation
            - The first for loop removes all the non-alphanumeric characters from the input string s.
            - In the second for loop, the str is traversed from both sides, the start and end, and each corresponding character is checked to be the same, if not return False as the str is not a palindrome

            Time Complexity: O(n)
            Space Complexity: O(1) extra space, O(n) space for the output
        """

        s_new = ""

        for c in s:
            if (ord(c) in range(48, 58)) or (ord(c) in range(65,91)) or (ord(c)in range(97,123)):
                s_new += c.lower()

        for i in range(len(s_new)//2):
            if s_new[i] != s_new[len(s_new)-1-i]:
                return False
        
        return True

def main():

    ans_obj = Solution()

    print(ans_obj.isPalindrome("Was it a car or a cat I saw?"))
    #print(ans_obj.isPalindrome("catss"))

    return

if __name__ == "__main__":
    main()