"""
34.45%

动态规划
状态转移方程
dp[x] 表示以 nums[x] 结尾的最长递增子串的长度
dp[x] = max(dp[x], dp[y] + 1), x > y, nums[x] > nums[y]
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        dp = [1] * size

        for x in range(size):
            # y需要小于x
            for y in range(x):
                if nums[x] > nums[y]:
                    dp[x] = max(dp[x], dp[y]+1)
        return max(dp)