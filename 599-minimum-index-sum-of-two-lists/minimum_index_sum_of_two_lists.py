"""
17.92%
"""

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        mi = -1
        result = []
        if len(list1) < len(list2):
            list1, list2 = list2, list1
        for index1, l1 in enumerate(list1):
            if l1 in list2:
                index2 = list2.index(l1)
                newindex = index1 + index2
                if newindex < mi or mi == -1:
                    mi = newindex
                    result[:] = []
                    result.append(l1)
                elif newindex == mi:
                    result.append(l1)
        return result