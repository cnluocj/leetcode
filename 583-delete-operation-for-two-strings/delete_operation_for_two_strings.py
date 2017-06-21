"""
58.55%

动态规划
"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1len, word2len = len(word1), len(word2)
        d = [[0] * (word2len + 1) for i in range(word1len + 1)]
        for x in range(word1len+1):
            for y in range(word2len+1):
                if x == 0 or y == 0:
                    d[x][y] = x + y
                elif word1[x-1] == word2[y-1]:
                    d[x][y] = d[x-1][y-1]
                else:
                    d[x][y] = min(d[x-1][y], d[x][y-1]) + 1
        return d[word1len][word2len]