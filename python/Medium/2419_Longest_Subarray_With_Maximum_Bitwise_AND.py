###########################################################################
# LeetCode Problem: 2419. Longest Subarray With Maximum Bitwise AND       #
# Date Solved: July 30th, 2025                                            #
#                                                                         #
# Thought Process:                                                        #
# - My first approach was brute force: find all possible subarrays, then  #
#   calculate the bitwise AND for each, finally return the length of the  #
#   longest subarray with the largest bitwise AND. This approach faces    #
#   time/memory limit exceeded, not surprising as it's O(n^3) time        #
#   complexity.                                                           #
# - The trick is to use the mathematical fact that if you AND two         #
#   integers together, the result is always less than or equal to the     #
#   smaller integer. Knowing this fact makes the problem near trivial.    #
#                                                                         #
# Pseudo Code:                                                            #
#                                                                         #
# First Approach:                                                         #
# 1. Find all the subarrays of the input array.                           #
# 2. Go through each subarray and calculate the bitwise AND for each.     #
# 3. If the bitwise AND is the largest seen so far, then store the length #
#    of the subarray as the largest seen so far.                          #
# 4. If the bitwise AND is equal to the largest seen so far, then check   #
#    if the length of the subarray is greater than the one seen earlier.  #
#    If it is, store it.                                                  #
# 5. Return the length of the longest subarray with the greatest bitwise  #
#    AND.                                                                 #
#                                                                         #
# Second ACCEPTED APPROACH:                                               #
# 1. Find the largest number in the input array.                          #
# 2. Count the consecutive occurrences of this number.                    #
# 3. Return the longest consecutive occurrence of the largest number seen.#
#                                                                         #
# Notes:                                                                  #
# - First medium problem in a long time.                                  #
# - `return(nums.count(max(nums)))` as a one-line solution doesn't work   #
#   due to the definition of a subarray. A subarray is a contiguous       #
#   sequence of elements within an array.                                 #
###########################################################################


# First Version
# Find all sub-arrays of input array nums
# calculate Bitwise AND of each sub-array
# return the length of the longest sub-array that has the largest bitwise AND
class Brute_Force_Solution:
    def extract_i_to_j(self, arr, i, j):
        l = []
        for k in range(i,j+1):
            l.append(arr[k])
        return(l)

    def longestSubarray(self, nums):
        n = len(nums)
        subarrays = []

        # generate all possible subarrays
        # this is what makes it O(n^3)
        for i in range(0, n):
            for j in range(i,n):
                # subarrays.append(nums[i:j+1])         this also takes O(n)
                subarrays.append(self.extract_i_to_j(nums, i, j))

        max_AND = 0 # max possible AND of any subarray
        max_len = 0 # max possible length of any subarray with max AND

        for arr in subarrays:
            arr_AND = arr[0]
            for ele in arr:
                arr_AND = arr_AND & ele
            
            if arr_AND > max_AND:
                max_AND = arr_AND
                max_len = len(arr)
            if (arr_AND == max_AND) and (len(arr) > max_len):
                max_len = len(arr)

        return max_len

# The key mathematical fact is that if two integeres are anded together the result is smaller than or equal to the smaller number!
# so essentially we need to just return the length of the longest subarray of the greatest number in the array
class Accepted_Solution:
    def longestSubarray(self, nums):
        max_num = max(nums)
        max_len = 0
        count = 0

        for i in nums:
            if i == max_num:
                count+=1
                if count > max_len:
                    max_len = count
            else:
                count = 0
        
        return max_len

def main():
    sol1 = Brute_Force_Solution()
    sol2 = Accepted_Solution()

    nums = [1,2,3,3,2,2]
    
    print(sol1.longestSubarray(nums))
    print(sol2.longestSubarray(nums))

    return(sol2.longestSubarray(nums))

if __name__ == "__main__":
    main()
