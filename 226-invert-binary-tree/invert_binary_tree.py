"""
12.66%
28.01%

一开始想复杂了
先转再递归也是可以的，更简洁了
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        # if root.left or root.right:
        #     if root.left:
        #         if root.left.left or root.left.right:
        #             self.invertTree(root.left)
        #     if root.right:
        #         if root.right.left or root.right.right:
        #             self.invertTree(root.right)
        #     root.left, root.right = root.right, root.left

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root