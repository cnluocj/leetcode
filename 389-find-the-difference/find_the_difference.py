"""
25.19%
"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for index in range(len(s)):
            t = t.replace(s[index], '', 1)
        return t
