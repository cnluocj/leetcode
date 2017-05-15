"""
8.68%

比较低效的方法，有待修改
"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) < k:
            return s[::-1]
        
        length = len(s)
        result = ''
        flag = False
        i = 0
        count = 0
        for i in range(length):
            flag = False
            if i % k == 0:
                flag = True
                temp = s[i:i+k]
                if count % 2 == 0:
                    result += temp[::-1]
                else:
                    result += temp
                count += 1
        if not flag:
            result += s[i:-1]
        return result
