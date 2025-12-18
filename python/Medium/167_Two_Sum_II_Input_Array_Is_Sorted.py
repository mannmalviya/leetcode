"""
LeetCode Problem: 167. Two Sum II - Input Array Is Sorted
Link:
- https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
- https://neetcode.io/problems/two-integer-sum-ii/question?list=neetcode150

Date Solved: 17th December, 2025

Thought Process: 
- See the function comments

Notes:
- 2nd NeetCode150 problem under: Two Pointers
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
            - We use two pointers to adjust the sum efficiently. If the current sum is too big, moving the right pointer left makes the sum smaller, if the sum is too small, moving the left pointer right makes the sum larger. This let's us quickly close in on the target without needing to check every pair.
        
            - Copied straight from the neetcode solution

            Time Complexity: O(n)
            Space Complexity: O(1)
        """

        lp = 0
        rp = len(numbers)-1

        while (lp < rp):
            sum = numbers[lp]+numbers[rp]
            if sum == target:
                return [lp+1, rp+1]
            if (sum < target):
                lp+=1
            else:
                rp-=1

        return []

    def twoSum_binary_search(self, numbers: List[int], target: int) -> List[int]:
        """
            - For every num in numbers we search the entire list after it to see if target-num exists in it, if it does then we return the index of both
                - The same idea was used in the brute force solution, except it searches the rest of the list end to end in a linar manner, so time complexity of O(n)
                - we could instead do binary search on the remaining list, as it is sorted, hence the time complexity for searching the rest of the list for target-num is O(logn)

            - This solution uses the information that the inp list numbers is sorted! by using binary search which can only be used to search an element in a sorted list
            - I was suprised I was able to actually write this soln.
            - It passes on LeetCode even though it's not O(n) time complex.


            Time Complexity: O(nlogn)
            Space Complexity: O(1)
        """
        
        def binary_search(arr, num):
            start = 0
            end = len(arr)-1

            while (start <= end):
                mid = (start + end) // 2

                if num == arr[mid]:
                    return mid
                elif num > arr[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            
            return -1

        for i in range(len(numbers)):
            j = binary_search(numbers[i+1:], target-numbers[i])
            if j != -1:
                return [i+1,j+i+2]

        return []

    def Brute_Force(self, numbers: List[int], target: int) -> List[int]:
        """
            - For every num in numbers I check if target-num exists in numbers, if it does I return the index of num & taget-num. We are always gauranteed a pair of numbers to add up to target to exist in the input list.
            - I notice that I am not using the fact that the input list `numbers` is sorted!
            - This solution times out on leetcode        
            
            Time Complexity: O(n^2)
            Space Complexity: O(1)
        """
        
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if (numbers[i] + numbers[j]) == target:
                    return [i+1,j+1]

        return []

def main():
    ans_obj = Solution()

    print(ans_obj.twoSum([2,7,11,15], 26))


    return

if __name__ == "__main__": main()
