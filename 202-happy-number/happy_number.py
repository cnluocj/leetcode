"""
70.49%
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0 or n == 1:
            return True
        x = [n]
        curr = n
        ishappy = False
        while True:
            digits = list(str(curr))
            curr = 0
            for d in digits:
                curr += int(d) ** 2
            x.append(curr)

            if curr == 1:
                ishappy = True
            if x.count(curr) >= 2:
                break

        return ishappy