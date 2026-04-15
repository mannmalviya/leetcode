"""
LeetCode Problem: 3896. Minimum Operations to Transform Array into Alternating Primes
Link:
- https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

Date Solved: April ?th, 2026
Total Time Spent: 

Thought Process:
- see below

Notes:
- Bi-Weekly Contest Problem
- I wasn't able to solve this during the contest
"""

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
            - The heart of the problem is in the `isPrime` function. The rest of the code is pretty self explanatory to this problem
            - I had first started with a brute force approach to determine whether a given number n is a prime by checking if any of the all possible pairs of numbers from 2..(n-1) would multiply to n 
            - This solution that implemented during the contest failed due to TIME LIMIT EXCEEDED

            Time Complexity: O()
            Space Complexity: O()
        """
        d = {}
        def isPrime(num: int) -> bool:
            if num == 1:
                return False
            if num == 0:
                return True
            
            n1 = 1
            n2 = num - 1
            while (n2 >= n1):
                prod = n1 * n2
                if prod == num:
                    return False
                elif prod > num:
                    n2 -= 1    
                elif prod < num:
                    n1 += 1

            d[num] = (n1, n2)
            return True
        
        def minOps(num: int, i: int) -> int:
            if i % 2 == 0:
                # make prime
                if isPrime(num):
                    return 0

                ops = 1
                while not isPrime(num + ops):
                    ops+=1
            else:
                # make non prime
                if not isPrime(num):
                    return 0

                ops = 1
                while isPrime(num + ops):
                    ops+=1

            return ops

        ops = 0
        for i in range(len(nums)):
            ops += minOps(nums[i], i) 

        return ops

        