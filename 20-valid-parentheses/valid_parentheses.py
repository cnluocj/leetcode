"""
71.84%
"""

import collections

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ma = {'(':')', '{':'}', '[':']'}
        stack = collections.deque()
        for x in s:
            if x in ma.keys():
                stack.append(x)
            else:
                if not stack:
                    return False
                else:
                    if ma[stack.pop()] != x:
                        return False
        if len(stack) != 0:
            return False
        return True