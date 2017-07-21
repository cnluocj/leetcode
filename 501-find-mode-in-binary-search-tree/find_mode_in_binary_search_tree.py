"""
78.38%
"""

from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None:
            return []

        queue = [root]
        values = []
        for node in queue:
            values.append(node.val)
            queue += [n for n in (node.left, node.right) if n is not None]
        
        max = 0
        result = []
        d = defaultdict(int)
        for v in values:
            d[v] += 1

            if d[v] > max:
                result[:] = []
                result.append(v)
                max = d[v]
            elif d[v] == max:
                result.append(v)
        return result