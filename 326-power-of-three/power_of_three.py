"""
16.53

参考答案
判断一个数是不是3的次方数
最直接的方法就是不停地除以3，看最后的余数是否为1
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n and n % 3 == 0:
            n /= 3
        return n == 1