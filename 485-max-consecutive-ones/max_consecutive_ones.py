"""
39.23%
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen = 0
        currlen = 0
        for num in nums:
            if num == 1:
                currlen += 1
                maxlen = max(maxlen, currlen)
            else:
                currlen = 0
        return maxlen