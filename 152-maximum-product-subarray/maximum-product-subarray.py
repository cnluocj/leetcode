"""
31.98%

动态规划

更简单的，空间复杂度 O(1)
m = mx = mn = nums[0]
for i in range(1, len(nums)):
    n = nums[i]
    mn, mx = min( n, n*mn, n*mx ), max( n, n*mx, n*mn )
    m = max(m, mx)
return m
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        max_dp = [0] * (size + 1)
        min_dp = [0] * (size + 1)
        result = 0

        for i in range(1, size + 1):
            if i == 1:
                max_dp[i] = nums[i-1]
                min_dp[i] = nums[i-1]
                result = nums[i-1]
            else:
                max_dp[i] = max(max_dp[i-1] * nums[i-1], min_dp[i-1] * nums[i-1], nums[i-1])
                min_dp[i] = min(max_dp[i-1] * nums[i-1], min_dp[i-1] * nums[i-1], nums[i-1])

            result = max(result, max_dp[i])

        return result