"""
49.08%
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        result = []
        r = set(nums1) & set(nums2)
        nums1_counts = collections.Counter(nums1)
        nums2_counts = collections.Counter(nums2)
        for x in r:
            m = min(nums1_counts[x], nums2_counts[x])
            result += ([x] * m)
        return result
