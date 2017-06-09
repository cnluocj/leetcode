"""
82.30%
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ma = {}
        for index, num in enumerate(numbers):
            if ma.has_key(num):
                return [ma[num]+1, index+1]
            ma[target-num] = index
        return ma