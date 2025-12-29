"""
LeetCode Problem: 557. Reverse Words in a String III
Link:
- https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

Date Solved: Dec 28th, 2025
Total Time Spent: 15mins

Thought Process: 
- See below function comments

Notes:
- Random Easy problem
"""

class Solution:
    def reverseWords_initial(self, s: str) -> str:
        """
            - Accumalate all character in a variable, `word` when a blank space ' ' is encountered add the reverse of the word to your output list. This sill give you the required sentence with each word reversed.
            - Maybe this method is considered cheating? as I use [::-1] to reverse each word
        
            Time Complexity: O(n)
            Space Complexity: O(n) for output string, O(1) extra space
        """

        result = ""
        word = ""
        for c in s:
            if c == " ":
                result += word[::-1] + c
                word = ""
            else:
                word += c

        return result + word[::-1]   

    def reverseWords_editorial_sol1(self, s: str) -> str:
        """
            - Ok maybe using prebuilt functions could be considered as cheating, so here's a solution that does the reversing of each word explicitly
            - Traverse the list to find the start and end indexes of each word in the string
            - Traverse each of the words backwards and add it to the required output string
            - This sol. is taken straight from the official leetcode editorial
            - Even though this is an official soln it only beast 6.25% in runtime (probably more efficient in other languages?)
            - Every character in the string is traversed twice. First, to find the end of the current word, and second to reverse the word and append it to the result. Thus the time complexity is, O(N+N)=O(N).
            
            Time Complexity: O(n) even though there are nested loops
            Space Complexity: O(n) for output list, O(1) extra space
        """

        result = []

        last_space_index= -1

        for char_index in range(len(s)):
            if s[char_index] == ' ' or char_index == len(s)-1:
                if char_index != len(s)-1:
                    iter = char_index - 1
                else:
                    iter = char_index

                while(iter > last_space_index):
                    result.append(s[iter])
                    iter-=1
                if char_index != len(s)-1:
                    result.append(' ')
                last_space_index = char_index

        return "".join(result)


    def reverseWords_editorial_sol2(self, s: str) -> str:
        """
            - This solution uses 2 pointers
            - Instead of traversing each word backwards like the prev editorial sol you could swap the first element and last element pointed to by 2 ptrs and then increment and decrement the ptrs and keep swapping them in each iteration.
            - taken from official editorial solution
            - beats 9.49% in runtime and 99.96% in memeory

            Time Complexity: O(n)
            Space Complexity: O(n) for output list
        """

        last_space_index = -1
        s = list(s)
        for char_index in range(len(s)):
            if s[char_index] == ' ' or char_index == len(s)-1:
                if char_index == len(s)-1: 
                    startIndex = char_index
                else: 
                    startIndex = char_index - 1 
                endIndex = last_space_index+1

                while (startIndex > endIndex):
                    tmp = s[endIndex]
                    s[endIndex] = s[startIndex]
                    s[startIndex] = tmp
                    startIndex -= 1
                    endIndex += 1
                last_space_index = char_index

        return "".join(s)

    def one_liner(self, s:str) -> str:
        """
            - Python One line solution for fun!
            - Eventhough this has the same time complexity as my initial solution, it still performs better by beating 100% of submissions
            
            Time Complexity: O(n)
            Space Complexity: O(n) extra space
        """

        return " ".join([word[::-1] for word in s.split()])

def main():
    ans_obj = Solution()

    print(ans_obj.one_liner("Mann is my Name"))
    print(ans_obj.reverseWords_editorial_sol2("Mann is my Name"))


    return

if __name__ == "__main__":
    main()