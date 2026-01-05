"""
LeetCode Problem: 1411. Number of Ways to Paint N x 3 Grid
Link:
- https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/?envType=daily-question&envId=2026-01-03

Date Solved: Jan 3rd, 2026
Total Time Spent: <=3hrs

Thought Process: 
- I initially thought this was a pure combinatorics problem, i.e., if I could find a mathematical function of n that counts the total number of ways to paint the nx3 grid. But after looking at the hints and comments on the problem, they all said using DP.
- 

- I had to look at both hints given in by LeetCode(the second hint didn't help at all!), and I peeked at one of the user comments which had a image of attaching a new row of cells to a prev row of cells.

Notes:
- Daily Challenge problem
- The hard part about this problem wasn't implementation but rather coming up with solution.
- Implementing the second optimized version in C++ gave beats 100% in runtime and 70% in memory!
- Basically my first hard problem on LeetCode!

"""

class Solution:
    def numOfWays_initial(self, n: int) -> int:
        """ 
            - 

            - This was my initial solution I came up with that passed. It beat 21% in runtime and 87% in memory. With a slight tweak I was able to improve it more(look at next function)
            
        
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        mod = 10**9 + 7

        num_ways = 12
        num_xcx = 6
        num_cxy = 6

        for i in range(1,n):
            num_ways = ((num_cxy)*4 + (num_xcx)*5)% mod
            prev_num_cxy = num_cxy
            num_cxy = num_cxy * 2 + num_xcx * 2
            num_xcx = prev_num_cxy * 2 + num_xcx * 3

        return num_ways
    
    def numOfWays_2(self, n: int) -> int:
        """

            Time Complexity: O()
            Space Complexity: O()
        """
        mod = 10**9 + 7

        num_xcx = 6
        num_cxy = 6

        for i in range(1,n):
            prev_num_cxy = num_cxy
            num_cxy = (num_cxy * 2 + num_xcx * 2)% mod
            num_xcx = (prev_num_cxy * 2 + num_xcx * 3)% mod

        return (num_cxy + num_xcx)% mod    


def main():
    return

if __name__ == "__main__":
    main()