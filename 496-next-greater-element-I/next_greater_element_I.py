"""
23.14%
"""

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """

        resutl = []
        for n1 in findNums:
            is_finded = False
            for n2 in nums:
                if is_finded and n2 > n1:
                    resutl.append(n2)
                    break
                if n1 == n2:
                    is_finded = True
            else:
                resutl.append(-1)
        return resutl