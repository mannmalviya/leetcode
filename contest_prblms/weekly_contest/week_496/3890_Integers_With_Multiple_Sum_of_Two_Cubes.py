"""
LeetCode Problem: 3890. Integers With Multiple Sum of Two Cubes
Link:
- https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/description/

Date Solved: April 7th, 2026
Total Time Spent: - (wasn't able to do in contest)

Thought Process:
- see below function comments
- My approach during the contest was basically a search approach: To find whether a given number x is good, I would iterate a from 1 to x**(1/3) and then check if (x - a**3)**(1/3) is a whole number (int and not float) but this method kept failing, I thought it was clever but it didn't work, because the cuberoot operation in python on even perfect cubes was giving some amount of decimal part:(
    and then just check for every number <=n is good or not from above and add to ans array

Notes:
- Weekly Contest Problem
- I looked at all the hint during review of this problem
- I also looked at peoples comments and solutions
"""

from typing import List

class Solution:
    def findGoodIntegers(self, n: int) -> List[int]:
        """
            - Taken directly from one of the ppls solutions
            - This is different from my brute force implementations because it doesn't have that last loop from 1 to n that checks if each of those numbers is good or not one by one
            
            Time Complexity: O(n^(2/3))
            Space Complexity: O(n^(2/3))
        """
        cubesum_freq = {}

        a = 1
        while a <= n**(1/3):
            b = a
            while a**3 + b**3 <= n:
                cubesum = a**3 + b**3
                cubesum_freq[cubesum] = 1 + cubesum_freq.get(cubesum_freq, 0)
                b += 1
            a += 1

        ans = [cubesum for cubesum, freq in cubesum_freq.items() if freq > 1]

        return ans

    def findGoodIntegers_brute_force(self, n: int) -> List[int]:
        """
            - This is a brute force solution, where I precompute the frequencies of all numbers that are a sum of a^3 + b^3 where n**(1/3) <= a,b <= n**(1/3)
            - Doesn't pass on LeetCode -- Time Limit Exceeded
        
            Time Complexity: O(n)
            Space Complexity: O(n^(2/3)) worse case we store every unique sum
        """

        cubesum_freq = {}

        for a in range(1, n**(1/3)):
            for b in range(a, n**(1/3)):
                cubesum = a**3 + b**3
                cubesum_freq[cubesum] = 1 + cubesum_freq.get(cubesum, 0)

        def isgood(num: int):
            if (num in cubesum_freq) and (cubesum_freq[num] > 1):
                return True
            else:
                return False

        ans = []
        for num in range(1, n+1):
            if isgood(num):
                ans.append(num)       

        return ans.sort()
    
    def brute_force_optimized(self, n: int) -> List[int]:
        """
            - can make small optimizations to above, a,b must lie within [1,1000] because cbrt(10^9) = 10^3. 10^9 is the bounds on n. 
            - So we can precompute a frequency map for all pairs (a,b)
            - still fails
            
            Time Complexity: O(n)
            Space Complexity: O(m) m is the number of distinct cube sums
        """

        cubesum_freq = {}

        for a in range(1, 1001):
            for b in range(a, 1001):
                cubesum = a**3 + b**3
                cubesum_freq[cubesum] = 1 + cubesum_freq.get(cubesum, 0)

        def isgood(num: int):
            if (num in cubesum_freq) and (cubesum_freq[num] > 1):
                return True
            else:
                return False

        ans = []
        for num in range(1, n+1):
            if isgood(num):
                ans.append(num)       

        return ans.sort()
    