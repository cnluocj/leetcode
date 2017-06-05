"""
34.58%
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        try:
            start = nums.index(target)
            end = start + nums.count(target) - 1 
            return [start, end]
        except:
            return [-1, -1]