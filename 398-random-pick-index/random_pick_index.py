"""
83.53%

能通过的方法，在pick的时候，时间复杂度是 O(n)
不能通过的方法，说是内存不够用，但是pick的时候时间复杂度是 O(1)

直到我看到了大神的答案
class Solution(object):
    def __init__(self, nums):
        self.indexes = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.indexes[num].append(i)

    def pick(self, target):
        return random.choice(self.indexes[target])

collections.defaultdict 能省内存吗？
不过也不能通过测试了
"""

import random

class Solution(object):

    # def __init__(self, nums):
    #     """
    #     :type nums: List[int]
    #     :type numsSize: int
    #     """
    #     self.valmaps = {}
    #     for index, num in enumerate(nums):
    #         if not self.valmaps.has_key(num):
    #             self.valmaps[num] = []
    #         self.valmaps[num] += [index]

    # def pick(self, target):
    #     """
    #     :type target: int
    #     :rtype: int
    #     """
    #     return random.choice(self.valmaps[target])

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        col = []
        for index, num in enumerate(self.nums):
            if target == num:
                col.append(index)
        return random.choice(col)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)