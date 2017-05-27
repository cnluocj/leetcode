"""
21.38%

有个答案
nums.sort(key= lambda x: 1 if x == 0 else 0)
服
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return 
        indexs = []
        for index, num in enumerate(nums):
            if num == 0:
                indexs.append(index)
        offset = 0 
        for index in indexs:
            num = nums[index-offset]
            nums.remove(num)
            nums.append(num)
            offset += 1
