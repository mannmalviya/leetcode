"""
LeetCode Problem: 1672. Richest Customer Wealth
Link:
- https://leetcode.com/problems/richest-customer-wealth/description/

Date Solved: Dec 28th, 2025
Total Time Spent: < 10mins

Thought Process: 
- very straightforward and easy question

Notes:
- Random Easy problem
"""

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
            - Calculate total wealth for each account
            - check if the current accounts wealth is greater than the max wealth seen so far, if its greater, then this is the new max wealth

            n is total number of elements in the 2D inp matrix
            Time Complexity: O(n) 
            Space Complexity: O(1) extra space
        """
        
        max_wealth = 0

        for account in accounts:
            wealth = 0
            for money in account:
                wealth += money
            if wealth > max_wealth:
                max_wealth = wealth

        return max_wealth

    def one_liner(self, accounts: List[List[int]]) -> int:
        """
            - Essentially does the same as above
            - calculate total wealth in each account
            - return the max wealth out of all 
            
            If M rows and max N elements in a row
            Time Complexity: O(M+N)
            Space Complexity: O(M)
        """

        return max([sum(account) for account in accounts])


def main():

    ans_obj = Solution()

    print(ans_obj.maximumWealth([[1,2,3], [3,2,1]]))
    print(ans_obj.one_liner([[1,2,3], [3,2,1]]))
    
    return

if __name__ == "__main__":
    main()
