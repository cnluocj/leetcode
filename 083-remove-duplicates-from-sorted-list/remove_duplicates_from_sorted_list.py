"""
60.36%
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        while current and current.next:
            next_node = current.next
            if next_node.val == current.val:
                current.next = next_node.next
            else:
                current = current.next
        return head