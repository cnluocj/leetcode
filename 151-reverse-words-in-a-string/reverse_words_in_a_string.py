"""
79.49%
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        s_array = s.split(' ')
        while True:
            try:
                s_array.remove('')
            except:
                break
        return ' '.join(s_array[::-1])