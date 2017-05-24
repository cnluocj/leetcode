"""
12.15%
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, su):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        return [s for s in self.paths(root) if sum(s) == su]

    def paths(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]
        tree_paths = [[root.val] + path for path in self.paths(root.left)]
        tree_paths += [[root.val] + path for path in self.paths(root.right)]
        return tree_paths