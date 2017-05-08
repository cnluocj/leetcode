"""
59.40%

其实是大数相加
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1_index = len(num1) - 1
        num2_index = len(num2) - 1
        if num1_index < 0:
            return num2
        if num2_index < 0:
            return num1
        carry = 0
        result = []
        while True:
            r = ''
            if num1_index >= 0 and num2_index >= 0:
                r = int(num1[num1_index]) + int(num2[num2_index]) + carry
            elif num1_index >= 0:
                r = int(num1[num1_index]) + carry
            elif num2_index >= 0:
                r = int(num2[num2_index]) + carry
            else:
                if carry > 0:
                   result.append(str(carry))
                break

            carry = 1 if r > 9 else 0
            r = r % 10
            result.append(str(r))

            num1_index -= 1
            num2_index -= 1

        return ''.join(result)[::-1]
