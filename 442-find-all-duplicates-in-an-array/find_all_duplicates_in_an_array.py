"""
41.25%
87.54%
"""

class Solution(object):
    # def findDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """

    #     mp = {}
    #     result = []
    #     for n in nums:
    #         try:
    #             mp[n] += 1
    #         except:
    #             mp[n] = 1
    #         else:
    #             result.append(n)
    #     return result

    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for n in nums:
            if nums[abs(n)-1] < 0:
                result.append(abs(n))
            else:
                nums[abs(n)-1] *= -1
        return result