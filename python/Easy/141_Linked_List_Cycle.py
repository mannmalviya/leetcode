"""
LeetCode Problem: 141. Linked List Cycle
Link:
- https://leetcode.com/problems/linked-list-cycle/description/

Date Solved: Feb 24th, 2026
Total Time Spent: 30mins

Thought Process: 
- Initially I was thinking about creating a second "annotated" linked list, which would be an exact copy of the input linked list except the ListNode object will contain one more field called 'visited' which will be set to False by default, creating this copied annotated linked list would take O(n) and then I would traverse this annotated linked list and for each node visited I will set visited field to True and if I ever visit a node that already has its visited property set to True then my function has found a cycle. THIS DOESN'T WORK!! because you cannot make the annotated copy of a linked list with a cycle as there is no node thats next node is Null!! Hence the function will never return.
- My next soln was accepted by LeetCode, traverse the Linked List for each node visited store the address of the node in a data struct., for each visited node check if that nodes address is already present in said data struct, if it is then that means theres a cycle in the linked list!
- The follow up question was to solve this problem in O(1) space complexity, I just looked at the NeetCode solution

Notes:
- NeetCode150: Under Linked Lists
"""

from typing import Optional

# Definition of singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle_initial(self, head: Optional[ListNode]) -> bool:
        """
            - See above thought process

            if n nodes in input linked list
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        if (not head or not head.next):
            return False

        curr = head.next
        visited = [head, curr]

        while(curr.next != None):
            curr = curr.next
            if curr in visited:
                return True
            visited.append(curr)

        return

    def hasCycle_optimization1(self, head: Optional[ListNode]) -> bool:
        """
            - Same as above but instead of using a list which has O(n) lookup, using a hash set which has O(1) lookup
        """
        if (not head or not head.next):
            return False

        curr = head.next
        visited = set({head, curr})

        while(curr.next != None):
            curr = curr.next
            if curr in visited:
                return True
            visited.add(curr)

        return
    
    def hasCycle_optimization2(self, head: Optional[ListNode]) -> bool:
        """
            - The follow up question was to solve this in O(1) space complexity!
            - This soln was taken from the NeetCode Editorial
            - I had to watch the video soln to understand why it works
            - This is the Fast & Slow pointer technique, aka "Flyod's Tortoise & Hare" algorithm

            Time Complexity: O(n)
            Space Complexity: O(1)
        """

        if (not head or not head.next):
            return False

        fast = head
        slow = head

        while (True):
            if fast.next == None or fast.next.next == None:
                break
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False