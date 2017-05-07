"""
28.41%

我又服了
if num == 0:
    return 0
return (num-1)%9+1
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        try:
            num = int(num)
        except:
            return 0

        if num < 10:
            return num
        
        while True:
            result = 0
            for d in str(num):
                result += int(d)
            if result < 10:
                return result
            else:
                num = result
        