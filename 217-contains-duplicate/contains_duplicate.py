"""
88.15%

有一个答案，我服
return len(nums) != len(set(nums))
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        result = {}
        for num in nums:
            if num in result:
                return True
            result[num] = 1
        return False
