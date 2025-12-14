"""
LeetCode Problem: 347. Top K Frequent Elements
Link:
- https://leetcode.com/problems/top-k-frequent-elements/description/ 
- https://neetcode.io/problems/top-k-elements-in-list/question?list=neetcode150

Date Solved: 27th November, 2025

Thought Process: 
- see below.

Notes:
- 5th Problem in Neetcode150
"""

from typing import List
from typing import Tuple, Dict


class Solution():
    def topKFrequent_Bucket_Sort_sol(self, nums: List[int], k: int) -> List[int]:
        """
            - This sol. is basically taken from neetcode.

            Time Complexity: O(n)
            Space Complexity: O()
        """
        num_freq = {}

        for num in nums:
            num_freq[num] = 1 + num_freq.get(num, 0)

        count_buckets = [[] for i in range(len(nums) + 1)]

        for num, freq in num_freq.items():
            count_buckets[freq].append(num)

        top_k_nums = []

        for i in range(len(count_buckets)-1, 0 , -1):
            for num in count_buckets[i]:
                top_k_nums.append(num)
                if len(top_k_nums) == k:
                    return top_k_nums
        return    


    def topKFrequent_minheap_sol(self, nums: List[int], k: int) -> List[int]:
        """
            - This sol. is basically taken from neetcode.

            Time Complexity: O()
            Space Complexity: O()
        """
        
        # Understand how Min Heaps work and how pythons heapqp works
        # https://dpythoncodenemesis.medium.com/understanding-pythons-heapq-module-a-guide-to-heap-queues-cfded4e7dfca

        return



    def topKFrequent_Sorting_sol(self, nums: List[int], k: int) -> List[int]:
        """
            - This sol. is basically taken from neetcode.
            - Start by making the num_freq map, then sort based on the numbers frequency.
            - Pop out the last K elements from the sorted list of number frequencies and return the numbers in a list(`top_k_nums`).
            
            Time Complexity: O(nlogn) len(nums)=n
            Space Complexity: O(n)
        """
        
        # create the number frequency/count map
        num_freq = {}

        for num in nums:
            num_freq[num] = 1 + num_freq.get(num, 0)

        freq_num_arr = []

        for num, freq in num_freq.items():     
            freq_num_arr.append((freq, num))

        freq_num_arr.sort()

        top_k_nums = []

        while len(top_k_nums) < k:
            _, num = freq_num_arr.pop()
            top_k_nums.append(num)

        return top_k_nums


    #--------------------------------------------------------------------------------------
    def topKFrequent_my_sol(self, nums: List[int], k: int) -> List[int]:
        """
            - This was my first(& only) solution. 
            - I make a hashmap, with num: freq (key value pairs), so a map between each unique number in `nums` & its frequency. This is the `num_freq` dictionary.
            - Then I just need to extract the top k most frequent numbers so I wrote a helper function `max_freq_num(map)` which given the hashmap of nums to its freq's will return the most frequent number and change its freq. to 0 so the next time `max_freq_num(map)` is called it will return the next most frequent number.
            - I call the max_freq_num(num_frq) function on the number frequency map k times and return the k most frequent elements in a list.
            
            Time Complexity: O(n*k) whrere len(nums)=n & k is given in the input
            Space Complexity: O(n)
        """
        
        # create the number frequency map
        num_freq = {}

        # this loop is O(n)
        for num in nums:
            num_freq[num] = 1 + num_freq.get(num, 0)
            
        top_k_nums = []

        # get the top k most frequent nums
        # This loop is O(n*k)
        for i in range(k):
            num, num_freq = self.max_freq_num(num_freq)
            top_k_nums.append(num)

        return top_k_nums
    
    def max_freq_num(self, map: Dict) -> Tuple[int, Dict]:
        """
            This is a helper function that returns the key with the max. value and sets the value to 0 in the map. The edited map is returned along with the key which has the max. value.
            
            Time Complexity: O(m) where m is size of map
            Space Complexity: O(1)
        """
        max_freq = 0
        max_freq_num = 0

        for num in map: 
            if map[num] > max_freq:
                max_freq = map[num]
                max_freq_num = num
                
        map[max_freq_num] = 0
        return max_freq_num, map
    

def main():
    ans = Solution()

    #print(ans.topKFrequent_Sorting_sol([0,0,1,3,3,3,4,55], 3))

    print(ans.topKFrequent_Bucket_Sort_sol([0,0,1,3,3,3,4,55], 2))

    #print(ans.max_freq_num({1:4, 2:10, 3:1}))

    return

if __name__ == "__main__":
    main()