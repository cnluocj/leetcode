"""
12.39%

大神答案
n=len(nums)
return n*(n+1)/2-sum(nums)

1+2+3+...+n = n*(n+1)/2

感觉又被压制了
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums = sorted(nums)
        for index, val in enumerate(nums):
            if index != val:
                return index
        return nums[-1] + 1