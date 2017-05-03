"""
39.42%
"""

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = 0
        for index, num in enumerate(nums):
            if index % 2 != 0 and num != pre:
                return pre
            pre = num
        if len(nums) % 2 != 0:
            return pre
        return None
