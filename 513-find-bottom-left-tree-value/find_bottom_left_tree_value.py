"""
25.30%

参考了一下答案
学会了，遍历树
(可以一边循环，一边在数组后面添加元素)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]

        for node in queue:
            queue += [item for item in (node.right, node.left) if item]
        return node.val