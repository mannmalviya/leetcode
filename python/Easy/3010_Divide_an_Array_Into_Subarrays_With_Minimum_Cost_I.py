"""
LeetCode Problem: 3010. Divide an Array Into Subarrays With Minimum Cost I
Link:
- https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description/?envType=daily-question&envId=2026-02-01

Date Solved: Feb 1st, 2026
Total Time Spent: 
- After spending 45mins with no progress I started to read the solution.

Thought Process: 
- 

Notes:
- Feb Daily Challenge problem
- I have the worst brain fog, it's absolutely embarrassing that I couldn't do this problem. I initially thought the solution was just `sum(sorted(nums)[:3])` but then it didn't pass the first test case where `nums = [10,3,1,1]` then I realised that I was forgetting that the subarrays must cover all the elements in nums.
- I thought for a while but I was unable to think of a simple way to do it. By the 45min mark out of frustration I was going to try and implement a brute force solution where I find all possible ways to divide nums into 3 subarrays and then find the cost for all the divisions and return the min cost but instead I chose to read the solution after which I was able to implement a solution that got accepted.
"""

from typing import List

class Solution():
    def minimumCost(self, nums: List[int]) -> int:
        """
            - The first element will always be the cost of the first subarray so the problem then becomes to find the two smallest numbers in the remaineder of the list(make sure you understand why!) 
            - you can find the two smallest numbers in O(n-1) time and don't need sorting

            Time Complexity: O(n)
            Space Complexity: O(1)

        """

        # find the two smallest numbers after the first number
        smallest = float('inf')
        smaller = float('inf')

        for num in nums[1:]:
            if num <= smallest:
                smaller = smallest
                smallest = num
            elif num < smaller:
                smaller = num

        return nums[0] + smaller + smallest

def main():
    ans = Solution()
    
    print(ans.minimumCost([10,3,1,1]))
    
    return

if __name__ == '__main__':
    main()
