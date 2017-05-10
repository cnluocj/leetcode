"""
84.99%

动态规划，其他网友写的，很有价值
"""

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        current, su = 0, 0
        for index in range(2, len(A)):
            if A[index] - A[index-1] == A[index-1] - A[index-2]:
                current += 1
                su += current
            else:
                current = 0
        return su