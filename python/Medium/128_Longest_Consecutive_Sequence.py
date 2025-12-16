"""
LeetCode Problem: 128. Longest Consecutive Sequence
Link:
- https://leetcode.com/problems/longest-consecutive-sequence/
- https://neetcode.io/problems/longest-consecutive-sequence/question

Date Solved: 14th December, 2025

Thought Process: 
-

Notes:
- 9th NeetCode150 problem
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        
            Time Complexity:
            Space Complexity:
        """

        # create the graph
        graph = {}

        for num in nums:
            graph[num] = None

        for num in nums:
            if num-1 in graph:
                graph[num-1]=num

        
        # traverse the graph to find longest consecutive sequence
        max_len = 0
        for node in graph:
            len = 1
            next_node = graph[node]
            while next_node != None:        
                len += 1
                next_node = graph[next_node]
            if len > max_len:
                max_len = len

        return max_len

    def Sorting(self, nums: List[int]) -> int:
        """


            Time Complexity: O(nlogn)
            Space Complexity:
        """
        nums.sort()

        max_len = 0
        count = 1

        print("sort(nums)", nums)

        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                count+=1
            else:
                if nums[i+1] != nums[i]:
                    if count > max_len:
                        max_len = count
                    count = 1

        return max_len

    def BruteForce(self, nums: List[int]) -> int:
        """
            In this bruteforce solution, for every number in nums we count how long a consecutive sequence you can find in nums. You can be extremely careful and count the number of operations in the worst case scenario and it comes to be in O(n^3) if you do the lookup for num+1 in a list as searching for a number in a list has time complex. O(n^3), this can be improved to O(n^2) by using a set which has lookup timecomplex. of O(1), thats how the neetcode brute force solution did it.
        
            Time Complexity: O(n^3)
            Space Complexity: O(1) extra space
        """

        max_len = 0

        for num in nums:
            len = 1
            while num+1 in nums:
                len+=1
                num+=1
            if len > max_len:
                max_len = len

        return max_len


def main():
    nums = [0,3,2,5,4,6,1,1]

    ans_obj = Solution()

    print(ans_obj.Sorting(nums))

    return    
    
if __name__ == "__main__":
    main()
