"""
33.11%
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen = 0
        cur = []
        nums = sorted(set(nums))
        for num in nums:
            if not cur:
                cur.append(num)
            else:
                if cur[-1] + 1 == num or cur[-1] == num:
                    cur.append(num)
                else:
                    cur[:] = []
                    cur.append(num)
            maxlen = max(maxlen, len(cur))
        return maxlen