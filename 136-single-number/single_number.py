"""
14.43%
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = {}
        for index, num in enumerate(nums):
            result[num] = result[num] + 1 if result.has_key(num) else 1
        for key, value in result.items():
            if value % 2 != 0:
                return key
        raise Exception('error nums')
 