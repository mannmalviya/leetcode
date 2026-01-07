"""
LeetCode Problem: 1161. Maximum Level Sum of a Binary Tree
Link:
- https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=daily-question&envId=2026-01-06

Date Solved: Jan 5th, 2026
Total Time Spent: <1hr on initial accepted soln

Thought Process: 
- Look at function comments below

Notes:
- Daily Challenge problem

"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum_recursive_DFS(self, root: Optional[TreeNode]) -> int:
        """
        - 

        Time Complexity: O()
        Space Complexity: O()
        """
        def make_sum_map(root: Optional[TreeNode], lvl: int, sum_map: dict):
            if root == None:
                return 

            sum_map[lvl] = root.val + sum_map.get(lvl, 0)
            curr_lvl = lvl

            lvl+=1
            make_sum_map(root.left, lvl, sum_map)
            lvl = curr_lvl
            lvl+=1
            make_sum_map(root.right, lvl, sum_map)

            return sum_map

        sum_map = make_sum_map(root, 1, {})

        max_lvl = 1
        max_sum = sum_map[1]

        for lvl in sum_map:
            if sum_map[lvl] > max_sum:
                max_lvl = lvl
                max_sum = sum_map[lvl]

        return max_lvl
    
    def maxLevelSum_iterative_DFS(self, root: Optional[TreeNode]) -> int:
        """
            -

            Time Complexity: O()
            Space Complexity: O()
        """
        stack = [(root, 1)]
        lvl_sum_map = {}

        while len(stack) != 0:
            node, lvl = stack.pop(0)
            if node:
                lvl_sum_map[lvl] = node.val + lvl_sum_map.get(lvl, 0)
                lvl+=1
                stack.insert(0, (node.right, lvl))
                stack.insert(0, (node.left, lvl))

        max_sum = lvl_sum_map[1]
        max_lvl = 1

        for lvl in lvl_sum_map:
            if max_sum < lvl_sum_map[lvl]:
                max_sum = lvl_sum_map[lvl]
                max_lvl = lvl

        return max_lvl

