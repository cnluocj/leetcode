"""
79.92%

也可以在初始化的时候把值都放进list里，然后再在list里choice
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import random

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        count = 0
        curr = self.head
        while curr:
            curr = curr.next
            count += 1
        r = random.randrange(count)
        curr = self.head
        for i in range(r):
            curr = curr.next
        return curr.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()