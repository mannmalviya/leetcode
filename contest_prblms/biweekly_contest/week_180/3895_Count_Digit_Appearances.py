"""
LeetCode Problem: 3895. Count Digit Appearances
Link:
- https://leetcode.com/problems/count-digit-appearances/

Date Solved: April 11th, 2026
Total Time Spent: < 10mins

Thought Process:
- see below

Notes:
- Bi-Weekly Contest Problem
"""

class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        """
            - Just count how many times the character digit shows up in the str(num) in nums
            - I did this in the contest

            Time Complexity: O(n) where n is the number of characters in the string representation of the elements of nums
            Space Complexity: O(1)
        """
        def cins(num, digit):
            count = 0
            for dig in num:
                if dig == digit:
                    count+=1
            return count

        count = 0
        for num in nums:
            count += cins(str(num), str(digit))

        return count

    def without_strings_approach(self, nums: list[int], digit: int) -> int:
        """
        
            Time Complexity: O(n) where n is the total number of digits in all numbers in nums
            Space Complexity: O(1) extra space
        """
        def helper(num: int, digit: int) -> int:
            """
                - returns the number of times digit shows up in num
            """
            count = 0
            while num > 0:
                if digit == (num % 10):
                    count += 1
                num = num // 10

            return count

        count = 0

        for num in nums:
            count += helper(num, digit)
        
        return count