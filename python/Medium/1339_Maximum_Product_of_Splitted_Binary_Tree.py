"""
LeetCode Problem: 1339. Maximum Product of Splitted Binary Tree
Link:
- https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/?envType=daily-question&envId=2026-01-07

Date Solved: Jan 6th, 2026
Total Time Spent: >2hrs probably and less than 3hrs

Thought Process: 
- Look at function comments below

Notes:
- Daily Challenge problem
- I ended up looking at the hints but I already knew what the hint was saying.
- I then out of frustatratyion put my code in to leet(the llm given by leetcode) and asked it why my code was timing out
- It told me something I already knew, I needed to maintain a way to store the sum of each subtree just once and not compute the sum of each subtree multiple times.
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree_eles(self, root: Optional[TreeNode]) -> int:

        stack = [root]
        tree_sum = 0

        while (len(stack) != 0):
            node = stack.pop(0)
            if node:
                tree_sum += node.val
                stack.insert(0, node.left)
                stack.insert(0, node.right)

        return tree_sum

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 10**9 + 7
        tree_sum = self.tree_eles(root)

        stack = [root]
        max_prod = 0

        while(len(stack) > 0):
            node = stack.pop(0)
            if node:
                subtree_sum = self.tree_eles(node.left)
                max_prod = max(max_prod, subtree_sum * (tree_sum-subtree_sum))
                
                subtree_sum = self.tree_eles(node.right)
                max_prod = max(max_prod, subtree_sum * (tree_sum-subtree_sum))                
                
                stack.insert(0, node.left)
                stack.insert(0, node.right)

        return max_prod % mod