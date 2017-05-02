"""
30.38%
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        result = l1
        while True:
            val = l1.val + l2.val
            t1 = val % 10
            t2 = val / 10

            l1.val = t1
            if t2 > 0:
                if not l1.next:
                    l1.next = ListNode(0)
                l1.next.val += t2
                if not l2.next:
                    l2.next = ListNode(0)
            else:
                if l1.next and not l2.next:
                    l2.next = ListNode(0)
                elif not l1.next and l2.next:
                    l1.next = ListNode(0)
                elif not l1.next and not l2.next:
                    break
            l1 = l1.next
            l2 = l2.next
        return result