"""
36.16%

好吧...
return  word.isupper() or word.istitle() or word.islower()
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        is_first_capital = False
        is_second_capital = False
        for index, letter in enumerate(word):
            letter = ord(letter)
            if index == 0:
                if 64 < letter < 97:
                    is_first_capital = True
            elif index == 1:
                if 64 < letter < 97:
                    if not is_first_capital:
                        return False
                    is_second_capital = True
            else:
                if is_first_capital and is_second_capital:
                    if not (64 < letter < 97):
                        return False
                elif not is_second_capital:
                    if 64 < letter < 97:
                        return False
        return True
