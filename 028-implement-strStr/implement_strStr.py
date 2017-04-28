"""
58.42%
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None:
            return -1
        return haystack.find(needle)
        