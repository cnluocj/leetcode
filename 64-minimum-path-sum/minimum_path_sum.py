"""
29.98%

动态规划
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        msize = len(grid)
        if msize == 0:
            return 0

        nsize = len(grid[0])
        if nsize == 0:
            return 0

        dp = [[0] * (nsize + 1) for i in range(msize + 1)]
        
        for i in range(1, msize+1):
            for j in range(1, nsize+1):
                if i == 1:
                    dp[i][j] = dp[i][j-1] + grid[i-1][j-1]
                elif j == 1:
                    dp[i][j] = dp[i-1][j] + grid[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
        return dp[msize][nsize]