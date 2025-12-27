"""
LeetCode Problem: 206. Reverse Linked List
Link:
- https://leetcode.com/problems/reverse-linked-list/
- https://neetcode.io/problems/reverse-a-linked-list/question?list=neetcode150

Date Solved: Dec 22nd, 2025
Total Time Spent: 8mins lol + little more time for understanding and implementing other ways to solve this problem(i.e., the 2 pointer method(straightforward), the recursion method)

Thought Process: 
- See below function comments

Notes:
- NeetCode150 problem 1 under Linked List
- This question was basically a freebie as I already have a lot of experience with linked lists. I'm surprised I haven't solved this one earlier!
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            - Traverse the input linked list, for each node insert it at the start of the new linked list, this will generate a reversed linked list.
        
            Time Complexity: O(n)
            Space Complexity: O(1) extra space, O(n) for the output reversed list
        """
        
        rev_head = None

        iter = head

        while (iter != None):
            node = ListNode(iter.val, rev_head)
            rev_head = node
            iter = iter.next
        
        return rev_head

    def reverseList_Recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            - 

            Time Complexity: O(n)
            Space Complexity: O(n)
        """

        head = self.reverseList_Recursive(head.next)



        return
    
    def reverseList_2pointer(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            - Use 2 pointers, both moving in the same direction from start to end, one pointer is one node ahead of the previous pointer.
            - traverse the linked list with the 2 pointers and each step, change the direction of the link
        
            Time Complexity: O(n)
            Space Complexity: O(1)
        """

        prev = None
        curr = head

        while (curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head = prev

        return head


def main():
    return

if __name__ == "__main__":
    main()
