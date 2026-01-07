"""
LeetCode Problem: 1339. Maximum Product of Splitted Binary Tree
Link:
- https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/?envType=daily-question&envId=2026-01-07

Date Solved: Jan 6th, 2026
Total Time Spent: >2hrs probably less than 3hrs?

Thought Process: 
- Look at function comments below

Notes:
- Daily Challenge problem

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