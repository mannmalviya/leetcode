"""
LeetCode Problem: 128. Longest Consecutive Sequence
Link:
- https://leetcode.com/problems/longest-consecutive-sequence/
- https://neetcode.io/problems/longest-consecutive-sequence/question

Date Solved: 14th December, 2025

Thought Process: 
- See comments in the functions
- I thought my solution in `My_Graph_DFS_longestConsecutive` was very clever and elegant, it fails to pass all the tests on LeetCode, with 'TIME LIMIT EXCEEDED' error, it's O(n^2), I initially wrongly concluded that it's O(n) time complexity.
- It's so funny, I thought I had two different approaches to this problem, one using a hashmap and the other using an adjacency list to maintain the graph, turns out both when coded out are exactly the same, in my head I thought they were different approaches but in implementation they are identical!
- The key hint that I needed to go from O(n^2) -> O(n) time complexity was to realize that a number is the start of a sequence only if num-1 doesn't exist in the list nums, and when implementing this u have to make sure to use a set because checking membership in a set is O(1) while checking in a list is O(n).

Notes:
- 9th NeetCode150 problem
"""

from typing import List

class Solution:
    def longestConsecutive_neetcode_soln(self, nums: List[int]) -> int:
        """
            - This one titled "Hash Set"
            - Basically further optimizes the Brute Force solution by only checking the length of the sequence if the num is the start of the sequence, by checking if num-1 exists in nums
            - It uses set(nums) to check if num-1 exists in nums because lookup in a set is O(1)

            Time Complexity: O(n)
            Space Complexity: O(n)
        """

        nums_set = set(nums)

        max_len = 0

        # suprisingly using `num in nums` times out  on Leetcode
        # But `num in nums_set` doesn't
        for num in nums_set:
            if (num-1) not in nums_set:
                length=1
                while((num+length) in nums_set):
                    length += 1
                if max_len < length:
                    max_len = length

        return max_len

    def longestConsecutive_my_soln(self, nums: List[int]) -> int:
        """
            - This soln. is extremely similar to my first implementation for this problem. (LOL and later I noticed it's basically identical to my "graph" solution with the optimization, I just wasn't thinking of it like that but when written out they are exactly identical, I just use different variable names for map and graph)
            - I make a hashmap where each element of nums is the key, and the corresponding value is the next number if it's present in nums, if not then the key is None.
            - Once this hashmap is created I go through each num in nums and find the length of the sequence that exists starting from that number in nums, while maintaining the length of the sequence in `l`
            - Up until here was my og implementation which is O(n^2) and hence didn't pass
            - The trick is to notice that we don't need to check sequences for each number in nums, notice that a number is only the start of a sequence if num-1 dne in nums, and you HAVE to check the membership of num-1 in set(nums) and not nums directly!
            - Membership checking is O(n) for a list and O(1) for a set

            - This soln is identical to the next one(with the graph), except it has the optimization to use set(nums) and to check if a num is the start of a sequence by checking if num-1 is in set(nums)

            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        nums_set = set(nums)

        # Create the hashmap
        map = {}

        for num in nums_set:
            if num not in map:
                map[num] = None
            if (num-1) in nums_set:
                map[num-1] = num

        max_len = 0

        # Traverse and find len of longest sequence
        for num in nums_set:
            if (num-1) not in nums_set: # <<-- This was the key hint
                l = 1
                next_num = map[num]
                while(next_num != None):
                    l+=1
                    next_num = map[next_num]

                if max_len < l:
                    max_len = l

        return max_len
    

    def My_Graph_longestConsecutive(self, nums: List[int]) -> int:
        """
            I first make a directed graph, stored in an adjacency list (here it's a dictionary where each number in num is a key and the value is either None or the next number that comes after it(that's also present in nums))

            Then starting from each node I traverse the graph going to the next node, then the next till I reach a node that's next node is None, all the while keeping a track of length of the chain traversed.
        
            Time Complexity: O(n^2)
            Space Complexity: O(n)
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
            I used pythons prebuilt function to sort the inp list nums in O(nlogn) time. 
            Then I keep checking if the next number continues the sequence or not, if it does, I increment `l` and if not I reset `l` and check whether this `l` was the longest one seen so far. I also handle duplicates, by skipping over them in the first if condition in the loop.

            Time Complexity: O(nlogn)
            Space Complexity: O(1) extra space (or O(n) depending on the sorting algorithm used)
        """
        if len(nums) == 0:
            return 0

        nums.sort() # O(nlogn)

        print(nums)

        max_l = 0
        l = 0

        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                continue
            if nums[i+1] == nums[i]+1:
                l+=1
            else:
                if max_l < l:
                    max_l = l
                l = 0

        return max(max_l+1, l+1)

    def BruteForce(self, nums: List[int]) -> int:
        """
            In this bruteforce solution, for every number in nums we count how long a consecutive sequence you can find in nums. You can be extremely careful and count the number of operations in the worst case scenario and it comes to be in O(n^3) if you do the lookup for num+1 in a list as searching for a number in a list has time complex. O(n^3), this can be improved to O(n^2) by using a set which has lookup timecomplex. of O(1), thats how the neetcode brute force solution did it.
        
            Time Complexity: O(n^3), can be optimized to O(n^2) if a set is used instead of a list
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

    print(ans_obj.longestConsecutive_neetcode_soln(nums))

    return    
    
if __name__ == "__main__":
    main()
