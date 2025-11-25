







class Brute_Force_Solution:
    def array_sum(self, arr):
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]

        return(sum)

    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        sums = []
        
        for i in range(0,n):
            for j in range(i, n):
                subarray = nums[i:j+1]
                sums.append(self.array_sum(subarray))

        return max(sums)


def main():
    return


if __name__ == "__main__":
    main()
