"""
40.83%
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        while n and n % 2 == 0:
            n /= 2
        
        return n == 1