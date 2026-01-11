"""
LeetCode Problem: 865. Smallest Subtree with all the Deepest Nodes
Link:
- https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/?envType=daily-question&envId=2026-01-09

Date Solved: Jan 9th, 2026
Total Time Spent: <1hr15mins

Thought Process: 
- Look at function comments below
- The problem didn't come with any hints, but it came with a note at the end which said this other problem named "1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/" is the exact same thing. 
- The name of this problem made me more confident in thinking in the direction of traversing the tree upwards

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
    def subtreeWithAllDeepest_initial(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
            - I first find the deepest nodes of the tree using iterative DFS, by maintaining the level of each node
            - While doing DFS I also simultaneously build a map that maps every node to its parent node
            - Since we are gauranteed by the problem that all nodes of the tree are unique, I traverse upwards from each of the deepest nodes and when I reach a common node while traversing the tree upwards(uisng the parent map I made in the previous step)
            - Also I am always gauranteed a common node, the root of the entire input tree!
            - This was my initial solution
            - Beats 100% in runtime and 5% in space

            (tbh I'm not too sure about below time & space comps, I just copied this from what the leetcode analyzer said my programs complexity was)
            Let V+E = N (V= number of nodes and E= numbeer of edges)
            Time Complexity: O(N)
            Space Complexity: O(N)
        """
        node_depths_map = {}

        stack = [(root, 1)]
        parent_node = {}

        # DFS + make the parent map
        while(len(stack) != 0):
            node, lvl = stack.pop(0)
            if node:
                node_depths_map[lvl] = node_depths_map.get(lvl, []) + [node]
                lvl+=1
                stack.insert(0, (node.left, lvl))
                stack.insert(0, (node.right, lvl))

                if node.left:
                    parent_node[node.left] = node
                if node.right:
                    parent_node[node.right] = node

        deepest_nodes = [node for node in node_depths_map[max(node_depths_map)]]

        # traverse the tree upwards from deepest nodes until common parent node found
        while(len(set(deepest_nodes)) != 1):
            for i in range(len(deepest_nodes)):
                deepest_nodes[i] = parent_node[deepest_nodes[i]]

        return deepest_nodes[0]


