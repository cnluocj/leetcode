"""
95.58%
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        see the answer
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return False

        map = {}
        for index, num in enumerate(nums):
            if num not in map:
                map[target-num] = index
            else:
                return [map[num], index]

print Solution().twoSum([2, 7, 11, 15], target=9)
    