"""
69.60%
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        sum = 1
        left_sum = self.maxDepth(root.left)
        right_sum = self.maxDepth(root.right)
        sum += max(left_sum, right_sum)
        return sum