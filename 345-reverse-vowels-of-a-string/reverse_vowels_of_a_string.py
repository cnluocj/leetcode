"""
24.19%
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = ('a', 'e', 'i', 'o', 'u')
        size = len(s)
        left, right = 0, size - 1
        ls = list(s)

        while left < right:
            is_left_vowels = (ls[left].lower() in VOWELS) 
            is_right_vowels = (ls[right].lower() in VOWELS)
            if not is_left_vowels:
                left += 1
            if not is_right_vowels:
                right -= 1
            if is_left_vowels and is_right_vowels:
                ls[left], ls[right] = ls[right], ls[left]
                left += 1
                right -= 1
        return ''.join(ls)