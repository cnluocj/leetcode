"""
63%
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = [[1]]
        for n in range(1, numRows):
            result.append(self.triangle(result[-1]))
        return result

    def triangle(self, t):
        ret = t[:]
        pre = t[:]
        for i in range(1, len(t)):
            ret[i] = pre[i] + pre[i-1]
        ret.append(1)
        return ret