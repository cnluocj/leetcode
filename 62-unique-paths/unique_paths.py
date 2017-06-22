"""
52.69%

动态规划
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        dp = [[0] * (n+1) for i in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 or j == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]