"""
61.41%
"""

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        if len(g) == 0 or len(s) == 0:
            return 0

        g = sorted(g)
        s = sorted(s)
        count = gindex = sindex = 0
        while True:
            if g[gindex] <= s[sindex]:
                gindex += 1
                sindex += 1
                count += 1
            else:
                sindex += 1
            if sindex >= len(s) or gindex >= len(g):
                break
        return count


