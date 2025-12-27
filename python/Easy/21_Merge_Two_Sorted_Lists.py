"""
LeetCode Problem: 206. Reverse Linked List
Link:
- https://leetcode.com/problems/merge-two-sorted-lists/
- https://neetcode.io/problems/merge-two-sorted-linked-lists/question?list=neetcode150 

Date Solved: Dec 23rd, 2025
Total Time Spent: 45mins + 20mins

Thought Process: 
- See below function comments

Notes:
- NeetCode150 problem 2 under Linked List
- 
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
            - For every element in list 2 we iterate through list1 and put it in the correct spot so that the entire linked list remains sorted
            - Even though at first you see nested loops, the worst case time complexity is still linear in the size of the lengths of list1 and list2 because we don't start search for the spot the number of list 2 needs to be inserted into in list1 from the  first element every time, we utilize the information that both input linked lists are sorted!

            Time Complexity: O(n+m)
            Space Complexity: O(n+m) for storing output
        """
        if list1 == None:
            return list2
        if list2 == None:
            return list1


        iter1 = list1
        iter1_prev = None
        iter2 = list2
        
        while iter2 != None:
            while iter1 != None and iter2.val > iter1.val:
                iter1_prev = iter1
                iter1 = iter1.next
            node = ListNode(iter2.val, iter1)
            if iter1_prev == None:
                list1 = node
                iter1_prev = node
            else:
                iter1_prev.next = node
                iter1_prev = node
            iter2 = iter2.next

        return list1
    
    def mergeTwoLists_naive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
            - I read both  linkedlists into a list, then sort that list using .sort() in O((N+M)log(N+M)) time, then convert the sorted list into a linked list and return it's head.
            - This solution doesn't utilize the fact that the input linked lists list1 & list2 are sorted.

            Where n and m are the lengths of list1 & list2
            Time Complexity: O((n+m)log(n+m))
            Space Complexity: O(n+m)
        """

        l = []

        iter1 = list1

        while (iter1 != None):
            l.append(iter1.val)
            iter1 = iter1.next

        iter2 = list2

        while (iter2 != None):
            l.append(iter2.val)
            iter2 = iter2.next

        l.sort()

        head = None

        for val in l[::-1]:
            node = ListNode(val, head)
            head = node

        return head

def main():
    return

if __name__ == "__main__":
    main()