"""
51.70%
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        result = temp = None
        while True:
            if not l1:
                result.next = l2
                break
            if not l2:
                result.next = l1
                break
            if l1.val < l2.val:
                if result is None:
                    result = ListNode(l1.val)
                    temp = result
                else:
                    result.next = ListNode(l1.val)
                    result = result.next
                l1 = l1.next
            else:
                if result is None:
                    result = ListNode(l2.val)
                    temp = result
                else:
                    result.next = ListNode(l2.val)
                    result = result.next
                l2 = l2.next

        return temp
