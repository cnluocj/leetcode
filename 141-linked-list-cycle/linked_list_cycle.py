"""
77.32%

参考了答案，很有意思的思路
可以用两个点去跑圈，一个快，一个慢
如果是循环的话，肯定会重叠
若果不是，就不是循环
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True
        return False