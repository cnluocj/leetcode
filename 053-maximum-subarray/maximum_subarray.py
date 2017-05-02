"""
91.40%
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = None
        temp = 0

        for num in nums:
            temp += num
            sum1 = temp if temp > sum1 else sum1
            if temp < 0:
                temp = 0
        return sum1
