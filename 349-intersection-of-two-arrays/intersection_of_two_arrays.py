"""
8.91%

看到有个答案
s1, s2 = set(nums1), set(nums2)
return list(s1&s2)

x & y 交集
x | y 并集
x - y 差集
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s = set()
        for num in nums1:
            if num in nums2:
                s.add(num)
        return list(s)