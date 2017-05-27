"""
21.62%

这个方法不高效
可以用找出一个个数大于n/2的数，会快点

看到一个答案
return sorted(nums)[len(nums)/2]
"""

import collections

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter(nums)
        maxcount = None
        maxnum = None
        for num, count in counter.items():
            if not maxnum:
                maxcount = count
                maxnum = num
            else:
                if count > maxcount:
                    maxcount = count
                    maxnum = num
        return maxnum