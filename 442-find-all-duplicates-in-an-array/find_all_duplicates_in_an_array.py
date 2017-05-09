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
        O(1) space not including the input and output variables

The idea is we do a linear pass using the input array itself as a hash to store which numbers have been seen before. We do this by making elements at certain indexes negative. See the full explanation here

http://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/

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