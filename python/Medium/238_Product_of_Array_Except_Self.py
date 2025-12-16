"""
LeetCode Problem: 238. Product of Array Except Self
Link:
- https://leetcode.com/problems/product-of-array-except-self/description/
- https://neetcode.io/problems/products-of-array-discluding-self/question?list=neetcode150

Date Solved: 14th December, 2025

Thought Process: 
- I was simply unable to solve this problem, all the solutions I could think of were O(n^2) time complexity.
- I looked at hint 1 on Leetcode (which actually happened to be hint3 on neetcode:/) which gave away the main idea of maintaining a prefix and sufix products to avoid recomputation. Once I understood this hint I was very quickly able to write the pseudo code and then the actual solution which passes.

Notes:
- 7th NeetCode150 Problem
"""

from typing import List

class Solution:
    def productExceptSelf_optimal(self, nums: List[int]) -> List[int]:
        """
            This is the most optimal solution. Not only O(n) time complex. but also O(1) space complex.!
            Doesn't use extra arrays to store the prefix and sufix arrays.

            We reuse the answer array to first hold the prefix products and then iterate over it once more and multiply in the sufix products hence bypassing the need for extra space for storing the prefix and sufix arrays.

            Time Complexity: O(n)
            Space Complexity: O(1)
        """

        answer = [1] * (len(nums))

        # fill in the prefix products:
        for i in range(len(nums)):
            if i == 0:
                continue
            answer[i] = answer[i-1] * nums[i-1]
        print(answer)
        
        # Multiply in the sufix products into the same answer array
        sufix = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= sufix
            sufix *= nums[i]

        return answer


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            This was my first implementation of the O(n) solution, after reading the hint that, we need to maintain a prefix and sufix array to avoid recomputing values.
        
            Time Complexity: O(n)
            Space Complexity: O(n)
        """

        # Compute Prefix array, O(n)
        pre = [1] * (len(nums))
        
        for i in range(len(nums)):
            if i == 0:
                pre[i] = 1
            else:
                pre[i] = pre[i-1] * nums[i-1]
        
        # Computer Sufix array, O(n)
        suf = [1] * (len(nums))

        for i in range(len(nums)-1 , -1, -1):
            if i == len(nums) - 1:
                suf[i] = 1
            else:
                suf[i] = suf[i+1] * nums[i+1]

        # Computer the answer, O(n)
        answer = []

        for i in range(len(nums)):
            answer.append(pre[i] * suf[i])

        return answer
    
    def Brute_Force(self, nums: List[int]) -> List[int]:
        """
            This is one of the ways to do the brute force solution. I was able to think of a few more ways to do O(n^2) soln. lol.
        
            Time Complexity: O(n^2)
            Space Complexity: O(1) extra space, O(n) space for the output
        """        
        answer = []

        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i != j:
                    prod = prod * nums[j]
            answer.append(prod)

        return answer

    def division(self, nums: List[int]) -> List[int]:
        """
            The question specifically asks to not use the division operator. But here's the soln. using division anyway. I read the NeetCode Soln. using division, wasn't able to come up with the entire working thing, so took help. I've already spent way too much time on this question :/
        
            The idea is to find the product of all the elements(which is O(n)), then traverse the list again and divide the total product by the current element and store that in the answers array.
            The only thing u need to be careful about is whether your inp. list nums contains 0's. There are 3 cases:

            1. No 0's: Then you just do the algorithm described above
            2. 1 0, then all elements in answer is 0 except the element which was the 0 in nums, it will now be the total prod of nums, aside from the 0
            3. 2 or more 0's: All elements of answer will be 0

            Time Complexity: O(n)
            Space Complexity: O(1) extra space, O(n) space for the output
        """

        answer = []

        # count number of 0's in nums
        count = 0
        for num in nums:
            if num == 0:
                count += 1

        answer = []
        match count:
            case 0:
                # No zeros in nums
                total_prod = 1
                for num in nums:
                    total_prod *= num

                for num in nums:
                    answer.append(int(total_prod/num))

            case 1:
                # 1 zero in nums
                total_prod = 1
                for num in nums:
                    if num != 0:
                        total_prod *= num

                for num in nums:
                    if num == 0:
                        answer.append(total_prod)
                    else:
                        answer.append(0)

            case _:
                # >= 2 zeros in nums
                answer = [0] * len(nums)

        return answer


def main():

    nums = [1,2,3,4]

    ans_obj = Solution()

    print(ans_obj.productExceptSelf_optimal(nums))

    return

if __name__ == "__main__":
    main()