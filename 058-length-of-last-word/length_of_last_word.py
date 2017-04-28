"""
60.15%
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        try:
            s = s.strip()
            return len(s.split(' ')[-1])
        except:
            return 0