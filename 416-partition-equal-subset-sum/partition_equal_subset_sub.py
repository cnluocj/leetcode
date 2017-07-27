"""
43.26%

任意子集合相加等于sum/2，就是true 
"""

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        sums = sum(nums)
        if sums % 2 != 0: 
            return False
        nset = set([0])
        for n in nums:
            for m in nset.copy():
                nset.add(n+m)
        return sums/2 in nset 