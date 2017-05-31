"""
21.25%
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        nums = sorted(list(set(nums)))
        n = 0
        for index, num in enumerate(nums):
            if num <= 0:
                n += 1
                continue
            if index+1-n != num:
                return index+1-n
        return nums[-1]+1