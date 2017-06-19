"""
57.40%
"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        for sub in t:
            if sub == s[0]:
                s = s[1:]
            if len(s) == 0:
                return True
        return False
