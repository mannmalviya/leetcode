"""
LeetCode Problem: 2483. Minimum Penalty for a Shop
Link:
- https://leetcode.com/problems/minimum-penalty-for-a-shop/?envType=daily-question&envId=2025-12-26

Date Solved: Dec 26th, 2025
Total Time Spent: an hour and some more for first solution

Thought Process: 
- The brute force soluion can be done quite easily in O(n^2) time complexity by calculating the penalty for each hourusing nested loops in a straightforward manner, I didn't implement the brute force solution.
- See below function comments

Notes:
- Daily LeetCode Challenge
"""

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
            - This solution maintains a prefix and suffix array for the penalties, and then adds them up to get the penalty for any given hour.
            - This was the first soution I came up with, although it's O(n), it's in the bottom 10% of runtime and memory of all submissions for this question.
            - Look at the next two functions for cleaner versions of this method of maintaining prefix and suffix arrays.
            
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        bc = [] # before closing
        count_n = 0

        for c in customers:
            bc.append(count_n)
            if c == 'N':
                count_n += 1

        bc.append(count_n)    
        ac = [] # after closing    
        count_y = 0

        for c in customers[::-1]:
            if c == 'Y':
                count_y += 1
            ac.append(count_y)
        ac = ac[::-1]
        ac.append(0)

        penalty = []
        for j in range(len(ac)):
            penalty.append(bc[j] + ac[j])

        minp = len(customers)
        minp_hr = 0

        for hr, p in enumerate(penalty):
            if p < minp:
                minp = p
                minp_hr = hr
        return minp_hr

    def bestClosingTime_optimization1(self, customers: str) -> int:
        """
            Combined creating the prefix and suffix arrays into a single loop
        """

        bc = [] # before closing
        count_n = 0

        ac = [] # after closing    
        count_y = 0

        for i in range(len(customers)):
            bc.append(count_n)
            if customers[i] == 'N':
                count_n += 1
            if customers[len(customers)-1-i] == 'Y':
                count_y += 1
            ac.append(count_y)

        bc.append(count_n)    
        ac = ac[::-1]
        ac.append(0)

        penalty = []
        for j in range(len(ac)):
            penalty.append(bc[j] + ac[j])

        minp = len(customers)
        minp_hr = 0

        for hr, p in enumerate(penalty):
            if p < minp:
                minp = p
                minp_hr = hr
        return minp_hr
    
    def bestClosingTime_optimization2(self, customers: str) -> int:
        """
            - This is the cleanest way to implement it with prefix and suffix arrays.
            - you don't actually need to maintain the arrays themselves!
        """
        count_n = 0
        count_y = 0

        penalty = len(customers)*[0]

        for i in range(len(customers)):
            penalty[i] += count_n
            if customers[i] == 'N':
                count_n += 1
            if customers[len(customers)-1-i] == 'Y':
                count_y += 1
            penalty[len(customers)-1-i] += count_y

        penalty.append(count_n)

        minp = len(customers)
        minp_hr = 0

        for hr, p in enumerate(penalty):
            if p < minp:
                minp = p
                minp_hr = hr
        return minp_hr