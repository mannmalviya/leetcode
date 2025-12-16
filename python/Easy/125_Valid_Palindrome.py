"""
LeetCode Problem:
Link:
- https://leetcode.com/problems/valid-palindrome/description/
- https://neetcode.io/problems/is-palindrome/question?list=neetcode150

Date Solved: 15th December, 2025

Thought Process: 
-

Notes:
- First problem under Two Pointers in NeetCode150
- 10th problem of NeetCode150
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
            This was my initial implementation

            <WRITE MORE>

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