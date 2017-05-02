"""
72.83%
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        words = s.split(' ')
        reverse_words = []
        for word in words:
            reverse_words.append(word[::-1])
        return ' '.join(reverse_words)