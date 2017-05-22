"""
13.21%


参考答案
1. 在不考虑数字的情况下，把所有字母情况算一遍，会比把给出的字符串全部遍历一遍快
return min([s.find(c) for c in string.ascii_lowercase if s.count(c)==1] or [-1])

2.
return min([s.find(c) for c,v in collections.Counter(s).iteritems() if v==1] or [-1])
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        try:
            x = min([s.find(key) for key, val in collections.Counter(s).iteritems() if val == 1])
        except:
            return -1
        return x 

