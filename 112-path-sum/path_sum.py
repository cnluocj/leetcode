"""
14.55%

可以有更优的方法，
这个方法是把所有路径都列出来，然后全部计算完，再判断是否有分支的值与参数相同,
太慢了
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, su):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return True if len([s for s in self.paths(root) if sum(s) == su]) > 0 else False
        
    def paths(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]
        tree_paths = [[root.val] + v for v in self.paths(root.left)]
        tree_paths += [[root.val] + v for v in self.paths(root.right)]
        return tree_paths