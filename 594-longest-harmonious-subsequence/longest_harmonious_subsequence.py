"""
24.55%

参考了答案的思路
"""

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        counts = collections.Counter(nums)
        result = 0
        for key in counts.keys():
            if counts[key+1]:
                result = max(result, counts[key] + counts[key+1])
        return result