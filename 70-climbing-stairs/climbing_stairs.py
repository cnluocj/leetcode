"""
33.39%
75.45%

实际是斐波拉契数列
第一种方法 时间，空间复杂度都是 O(n)
第二种递推法更厉害，不需要空间换时间，时间复杂度 O(n)，空间复杂度 O(1)

至于这题为什么动态转移方程是斐波拉契
Because from the [n-1] point, we can take one single step to reach [n]. 
And from the [n-2] point, we could take two steps to get there. 
There is NO overlapping between these two solution sets, because we differ in the final step.
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # x = {1:1, 2:2}
        # for i in range(3, n+1):
        #     x[i] = x[i-1] + x[i-2]
        # return x[n]

        if n < 2:
            return n
        prev, curr = 1, 2
        for i in range(3, n+1):
            prev, curr = curr, prev + curr
        return curr