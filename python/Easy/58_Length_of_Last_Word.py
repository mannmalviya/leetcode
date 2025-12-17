
"""
LeetCode Problem: 58. Length of Last Word
Link:
- https://leetcode.com/problems/length-of-last-word/description/

Date Solved: 16th December

Thought Process: 
- see comment in function

Notes:
- Lol randomly did this easy, so that I have a streak on my leetcode greengraph :p
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
            The .split() python function takes the input string and splits it into substrings based on a dilimeter(which by default is a blank space), and puts the substrings in a list. I then simply return the length of the last element in the list.                        

            .split() runs in O(n) time complexity

            Time Complexity: O(n)
            Space Complexity: O(n)
        """

        words = s.split()
        return(len(words[len(words)-1]))

    def lengthOfLastWord_NoHelp(self, s:str) -> int:
        """
            A solution that doesn't use the .split() helper function
        
            I keep track of the wordlength till a white space is encountered. If I encouneter a white space I store the word lenth in `last_word_len`. I had to add an extra if block to handle the case when you have multiple white spaces in a row. And I added a white space at the end of the inp string `s` so that we always return the last words length, because if if the last char in the str s is a character then `last_word_len` is still holding the length of the last to last word as it hasn't been updated, adding a white space at the end helps with that.

            Time Complexity: O(n)
            Space Complexity: O(1) extra space
        """
        last_word_len = 0
        word_len = 0

        space_seen = False

        s+=' '  # This is so jank bro:/

        for c in s:
            if space_seen and c != ' ':
                word_len = 1
                space_seen = False
                continue
            if c == ' ':
                last_word_len = word_len
                space_seen = True
            else:
                word_len += 1

        return last_word_len

def main():
    ans_obj = Solution()

    print(ans_obj.lengthOfLastWord_NoHelp("luffy is still joyboy"))

    return

if __name__ == "__main__":
    main()
