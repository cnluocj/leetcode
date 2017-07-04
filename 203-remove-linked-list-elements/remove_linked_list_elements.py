"""
68.89%
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre, curr = None, head
        while curr:
            if curr.val == val:
                if pre:
                    if curr.next:
                        pre.next = curr.next
                    else:
                        pre.next = None
                else:
                    head = curr.next
                curr = curr.next
            else:
                pre, curr = curr, curr.next
        
        return head