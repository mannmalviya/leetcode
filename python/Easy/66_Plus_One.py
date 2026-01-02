"""
LeetCode Problem: 66. Plus One
Link:
- https://leetcode.com/problems/plus-one/description/?envType=daily-question&envId=2026-01-01

Date Solved: Dec 31st, 2025
Total Time Spent: approx 14 mins

Thought Process: 
- Look at function comments below

Notes:
- Daily Challenge problem
"""

from typing import List

class Solution:
    def plusOne_initial(self, digits: List[int]) -> List[int]:
        """
            - I first read the number from the list into a integer
            - I add one to the integer
            - I store the integer back into a list, by converting it into a string and then parsing the string character by character
            - This was my first solution to the problem
            
            Let the input list `digits` have n elements, i.e., len(digits) = n
            Time Complexity: O(n) 
            Space Complexity: O(1) extra space, O(n) to store the output list
        """
        number = 0

        # Read the number into an integer
        for placevalue, digit in enumerate(digits[::-1]):
            number += digit * (10**placevalue)

        number += 1
        new_num_digits = []

        for digit in str(number):
            new_num_digits.append(int(digit))

        return new_num_digits
    
    def plusOne_second(self, digits: List[int]) -> List[int]:
        """
            - In this solution I still read the number from the list into an integer
            - Then increment the integer by 1
            - But instead of making it a string and then iterating over each character to store into the output lit, I keep dividing the number by 10, the remainder gives you the first digit every time and the quotient is the rest of the number after removing the first digit, you can keep repeating this till you have read each digit of the number
            - This was the 2nd sol I came up with!
            
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        number = 0

        for placevalue, digit in enumerate(digits[::-1]):
            number += digit * (10**placevalue)

        number += 1

        result_digits = []    

        while(number > 0):
            digit = number % 10
            number = number // 10
            result_digits.insert(0, digit)

        return result_digits

    def plusOne_third(self, digits: List[int]) -> List[int]:
        """
            - In this implementation I don't read the
            - This was the 3rd and final sol I implemented, I read the posted sols for this one
            
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        if len(digits) == 0:
            return digits

        index = len(digits) - 1
        while(digits[index] == 9 and index >= 0) :
            digits[index] = 0
            index -= 1
        
        if index < 0:
            digits.insert(0, 1)
        else:
            digits[index] += 1

        return digits

def main():
    ans_obj = Solution()

    print(ans_obj.plusOne_third([]))

    return

if __name__ == "__main__":
    main()