"""
LeetCode Problem: 944. Delete Columns to Make Sorted
Link:
- https://leetcode.com/problems/delete-columns-to-make-sorted/description/?envType=daily-question&envId=2025-12-20

Date Solved: 20th December, 2025
Total Time Spent: 50mins

Thought Process: 
- See below function comments

Notes:
- Dec 20th's LeetCode Daily Problem
"""

from typing import List

class Solution:
    def minDeletionSize1(self, strs: List[str]) -> int:
        """
            - After looking at one of the solns, I removed the sorting each column to check if the column is in lexicographic order which was taking nlogn time to just checking if the next char is greater than the prev char(defn of lexicographic order), this hence takes O(n) time.

            If the number of strings is n (len(strs)=n) and the length of the longest string is m(all strings of the same lenght lol).

            Time Complexity: O(m*n)
            Space Complexity: O(m*n)
        """

        # Make a list of columns
        columns = ["" for i in range(len(strs[0]))]

        for s in strs:
            for i, c in enumerate(s):
                columns[i] += c

        # count the number of columns that are not in increasing lexicographic order
        count = 0

        for s in columns:
            for i in range(len(s)-1):
                if s[i] > s[i+1]:
                    count += 1
                    break
            
        return count

    def minDeletionSize2(self, strs: List[str]) -> int:
        """

            - Try a solution where you don't need to store the columns, and instead just traverse the input strs wrt a column instead of the normal row traversal.
        
        
            Time Complexity:
            Space Complexity: O(1) extra space
        """

        # TODO

        return

    def minDeletionSize_my_sol(self, strs: List[str]) -> int:
        """
            - This was the first solution that came to my mind.
            - We essentially need to return the number of columns that are not sorted.
            - So first we extract all the columns after writing the words one below the other.
            - Then we count the number of these columns that are not sorted and return that count.
            - This solution was accepted on LeetCode.
            
            If the number of strings is n (len(strs)=n) and the length of the longest string is m(all strings of the same lenght lol).

            Time Complexity: O(m*nlogn)
            Space Complexity: O(m*n)
        """
        
        # Make a list of columns
        columns = ["" for i in range(len(strs[0]))]

        for str in strs:
            for i, c in enumerate(str):
                columns[i] += c

        # count number of colums that are not sorted
        count = 0

        for s in columns:
            # check if string s is sorted
            if list(s) != sorted(s):
                count+=1

        return count


def main():
    ans_obj = Solution()

    print(ans_obj.minDeletionSize(["abc","bac", "ccc"]))

    return

if __name__ == "__main__":
    main()