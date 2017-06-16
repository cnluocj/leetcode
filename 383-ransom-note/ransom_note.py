"""
28.85%

更简单
for c in set(ransomNote):
    if ransomNote.count(c)>magazine.count(c):
        return False
return True
"""

import collections

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_counter = collections.Counter(ransomNote)
        magazine_counter = collections.Counter(magazine)
        for key, value in ransom_counter.items():
            if key in magazine_counter.keys() and magazine_counter[key] >= value:
                continue;
            else:
                return False
        return True