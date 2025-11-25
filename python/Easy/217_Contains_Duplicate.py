"""
LeetCode Problem: 217. Contains Duplicate
Link: 
- https://leetcode.com/problems/contains-duplicate/
- https://neetcode.io/problems/duplicate-integer/question

Date Solved: November 24th, 2025 (resolved)

Thought Process / Approach: 
- explaine in the function comments
- Another soln. is to sort the list at the start and then iterate through it to see if any consecutive elements are the same. This has:
Time Comp.: O(nlogn) (nums.sort() probably uses Quick Sort internally?) 
Space Comp.: O(1) or O(n) depending on the sorting algo.

Notes:
- Resolved this very intro basic problem. 
- This is the first problem in the Neetcode150 roadmap! Starting this roadmap today. 
- 1st Neetcode150 prblm.
"""

from typing import List

class Solution():
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
            The trick to solve this prblm in O(n) is to use a hash(dictionary in python), because the lookup time to check if an element is in it the hash is O(1)
        
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        dict = {}
    
        for i in nums:
            if i not in dict:   # checking if ele in a dict is O(1) unlike O(n) in a list
                dict[i] = 1
            else: 
                return True

        return False


    def brute_force1(self, nums: List[int]) -> bool:
        """
            Go through the list one element at a time, for each element check if another instance of it exists, if it does, return True, if not keep looping. Return False at the end, which is hit when no duplicates for any element are found.
        
            Time Complexity: O(n^2)
            Space Complexity: O(1)
        """

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == nums[i]:
                    return True
        return False

    def brute_force2(self, nums: List[int]) -> bool:
        """
            Another brute force solution idea is to maintain a sperate list. Iterate through nums and check if this other list contains the current number, if it does return True, if not add it to this other list and continue looping over the remaining list. Return False at the end

            Time Complexity: O(n^2)
            Space Complexity: O(n)
        """
        tmp = []

        for i in nums:
            if i in tmp:
                return True
            else:
                tmp.append(i)

        return False

def main():
    obj = solution()

    print(obj.brute_force1([1,4,2,3,4]))
    print(obj.brute_force2([1,4,2,3,4]))

    return 

if __name__ == "__main__":
    main()
