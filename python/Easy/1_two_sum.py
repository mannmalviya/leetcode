"""
LeetCode Problem: 1. Two Sum
Link:
- https://leetcode.com/problems/two-sum/description/
- https://neetcode.io/problems/two-integer-sum/question?list=neetcode150

Date Solved: 24th November, 2025 (resolved)

Thought Process: 
- See below.

Notes:
- Humble beginnings. Resolved this, I think I've done this 2-3times in the pasts.
- 3rd prblm in Neetcode150
- Michael was the one to explain the O(n) solution to me a while back. I was only able to find O(n^2) brute force solution by myself.
"""

from typing import List

class Solution():
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            This is a very neat solution that uses a hashmap, and iterates over the list of nums only once. It goes over the list and for each number it checks if target minus that number exists in the hashmap, if it does then we have found the pair that adds to target, if not we add the number, as the key and the index as the value, in to the hash map. 
    
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        map = {}

        for i, num in enumerate(nums):
            if (target - num) in map:
                return [map[target-num], i]
            else:
                map[num] = i

        return
    
    def brute_force(self, nums: List[int], target: int) -> List[int]:
        """
            Generate all possibe 2 element subsets of the list and go over each of them to see which one adds up to `target`.
        
            Time Complexity: O(n^2)
            Space Complexity: O(1)
        """

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i , j]

        return

def main():
    return

if __name__ == "__main__":
    main()
