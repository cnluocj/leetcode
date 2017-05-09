"""
77.45%

这个看了下网友的答案，我又折服了，都忘记了set可以这么用
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1, len(nums)+1)) - set(nums))
        