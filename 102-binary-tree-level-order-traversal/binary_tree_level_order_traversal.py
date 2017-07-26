"""
82.56%
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.setupLevels([root], result)
        return result
    
    def setupLevels(self, nodes, result):
        nodeValues = []
        childNodes = []
        if not nodes:
            return result
        for node in nodes:
            if node is not None:
                nodeValues.append(node.val)
                if node.left:
                    childNodes.append(node.left)
                if node.right:
                    childNodes.append(node.right)
        if nodeValues:
            result.append(nodeValues)
        self.setupLevels(childNodes, result)