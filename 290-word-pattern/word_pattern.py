"""
51.91%
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_array = str.split(' ')
        if len(pattern) != len(str_array):
            return False
        pattern_map = {}
        str_map = {}
        for index, letter in enumerate(pattern):
            if pattern_map.has_key(letter) and str_array[index] != pattern_map[letter]:
                return False
            if str_map.has_key(str_array[index]) and str_map[str_array[index]] != letter:
                return False
            pattern_map[letter] = str_array[index]
            str_map[str_array[index]] = letter
        return True
