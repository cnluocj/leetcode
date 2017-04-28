"""
31.05%
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        for index, num in enumerate(nums):
            if num >= target:
                return index
        return len(nums)