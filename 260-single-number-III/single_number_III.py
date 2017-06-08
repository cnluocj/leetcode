"""
5.32%
"""

import collections

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        counter = collections.Counter(nums)
        for num, count in counter.items():
            if count == 1:
                result.append(num)
            if len(result) == 2:
                break
        return result