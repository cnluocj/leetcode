"""
34.06%

字符统计，单词的字谜变换（anagram）是指与其字母个数相同只是顺序不同的单词
可以使用 Counter 做比较
"""

from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if s == "" or s is None:
            return []

        psize = len(p)
        ssize = len(s)
        result = []
        pcounter = Counter(p)
        scounter = None
        for index, value in enumerate(s):
            if index + psize <= ssize:
                if scounter is None:
                    scounter = Counter(s[index:index+psize])
                else:
                    scounter[s[index-1]] -= 1
                    scounter[s[index+psize-1]] += 1
                    if scounter[s[index-1]] == 0:
                        del scounter[s[index-1]]
                if pcounter == scounter:
                    result.append(index)
            else:
                break
        return result

def main():
    s = Solution()
    print s.findAnagrams('abcdefgabcdefgabcdefgabcdefgabcdefg', 'abcdefg')

if __name__ == '__main__':
    main()