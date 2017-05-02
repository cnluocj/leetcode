"""
56.49%
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row = 'qwertyuiop'
        second_row = 'asdfghjkl'
        third_row = 'zxcvbnm'

        if not words:
            return words

        same_row_words = []
        for word in words:
            row = 0
            for letter in word:
                if letter.lower() in first_row:
                    row = 1 if (row == 0 or row == 1) else -1
                elif letter.lower() in second_row:
                    row = 2 if (row == 0 or row == 2) else -1
                else:
                    row = 3 if (row == 0 or row == 3) else -1

            if row != -1:
                same_row_words.append(word)
        return same_row_words

