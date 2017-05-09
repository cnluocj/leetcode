"""
41.25%
"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        mp = {}
        result = []
        for n in nums:
            try:
                mp[n] += 1
            except:
                mp[n] = 1
            else:
                result.append(n)
        return result