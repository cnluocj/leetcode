"""
46.18%

状态转移方程
dp[i] = max(dp[i-2]+n[i-1], dp[i-1])
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        elif size == 1:
            return nums[0]
        elif size == 2:
            return max(nums[0], nums[1])

        prev, curr = 0, nums[0]
        for i in range(2, size+1):
            prev, curr = curr, max(prev + nums[i-1], curr)
        return curr