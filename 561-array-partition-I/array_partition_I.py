"""
27.53%

已经排序完了，就不需要再比较了
排序后，从第0个开始，每两步相加一次
for i in range(0,len(nums),2):
    counter += nums[i]
"""

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)

        temp_list = []
        result = 0
        for index, num in enumerate(nums):
            temp_list.append(num)
            if index % 2 != 0:
                result += min(temp_list)
                temp_list = []
        return result
