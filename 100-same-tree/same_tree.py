"""
58.14%
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None:
            if q is None:
                return True
            else:
                return False
        if q is None:
            if p is None:
                return True
            else:
                return False
        if isinstance(p, TreeNode) and isinstance(q, TreeNode):
            if p.val == q.val:
                leftIsSame = self.isSameTree(p.left, q.left)
                if leftIsSame:
                    rightIsSame = self.isSameTree(p.right, q.right)
                    if rightIsSame:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
