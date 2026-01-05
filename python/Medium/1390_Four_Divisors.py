"""
LeetCode Problem: 1390. Four Divisors
Link:
- https://leetcode.com/problems/four-divisors/description/?envType=daily-question&envId=2026-01-04

Date Solved: Jan 4th, 2026
Total Time Spent: NA

Thought Process: 
- Look at function comments below

Notes:
- Daily Challenge problem
- I basically just ended up looking at the solution for the main idea in this problem of being able to find all divisors for a number n in O(sqrt(n)) time and even then I don't think I fully understood it.

"""

from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        """
            - The main idea is in the part of finding all the factors for a number n, the naive apporach checks if each number in the range [1,n/2] is a factor of n BUT the trick is that we only need to check the numbers in the range [1,sqrt(n)] and if a number x in that range is a factor then immediately the number n/x is also a factor(also make sure n/x != x).

            If len(nums) = n and the biggest element in nums is m
            Time Complexity: O(n*sqrt(m))
            Space Complexity: O(1)
        """
        total_divs_sum = 0
        
        for num in nums:
            divs_sum = 1 + num
            num_divs = 2
            for d in range(2, int(num**0.5)+1):
                if num%d == 0:
                    num_divs += 1
                    divs_sum += d
                    if num//d != d: # <<-- this if does the perfect square handling
                        num_divs += 1
                        divs_sum += num//d
            if num_divs == 4:
                total_divs_sum += divs_sum

        return int(total_divs_sum)
    
    def sumFourDivisors_Optimized(self, nums: List[int]) -> int:
        """
            - Same as above but with a small optimization, if for a given number we find that its has more than 4 divisors we stop searching for more divisors of that number and move on to the next num.

            Same Time and Space complexity as above.
        """
        total_divs_sum = 0
        
        for num in nums:
            divs_sum = 1 + num
            num_divs = 2
            for d in range(2, int(num**0.5)+1):
                if num_divs > 4:    # <<<--- optimization
                    break
                if num%d == 0:
                    num_divs += 1
                    divs_sum += d
                    if num//d != d:
                        num_divs += 1
                        divs_sum += num//d
            if num_divs == 4:
                total_divs_sum += divs_sum

        return int(total_divs_sum)        
    
    def sumFourDivisors_Brute_Force(self, nums: List[int]) -> int:
        """
            - For every element in nums I find all of its divisors and the sum of the divisors
            - If the number of divisors equals 4 then I add their sum to my running sum for the result that must be returned
            - The way I find the divisors of a given number n is by trying/checking every number from 1 to n/2(notice that all numbers between n/2 and n can automatically be ruled out for being divisors!) to be divisor of n (if their modulo is 0). 
            - But this method of finding all divisors for a number n will take O(n/2)=O(n) time

            If len(nums) = n and the biggest element of nums is m
            Time Complexity: O(n*m)
            Space Complexity: O(1)
        """
       
        result_sum = 0

        for num in nums:
            num_divs = 2    # 1 and the number itself are always divisors for all numbers
            divs_sum = 1+num
            for div in range(2, num//2+1):
                if num%div == 0:
                    num_divs+=1
                    divs_sum+=div
            if num_divs == 4:
                result_sum+= divs_sum


        return result_sum

def main():
    return

if __name__ == "__main__":
    main()
