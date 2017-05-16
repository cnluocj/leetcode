"""
91.55%
"""

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return '0'

        n = abs(num)
        result = ''
        while n:
            result += str(n % 7)
            n /= 7
        result = result[::-1]
        return result if num >= 0 else '-'+result