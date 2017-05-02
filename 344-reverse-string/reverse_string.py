"""
45.05%

看了个答案可以这样
return s[::-1]
技不如人甘拜下风
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        stack = []
        for x in s:
            stack.append(x)
        s = ''.join(stack[::-1])
        return s
    