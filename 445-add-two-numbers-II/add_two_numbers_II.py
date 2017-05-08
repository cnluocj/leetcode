"""
41.96%

我这个太复杂了
其实可以把链表转成整数，然后求和，然后再转成链表
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

        def reverse(li):
            reverse_list = []
            while li:
                reverse_list.append(li.val)
                li = li.next
            reverse_list = reverse_list[::-1]

            l = result = None
            for x in reverse_list:
                if l is None:
                    l = result = ListNode(x)
                else:
                    l.next = ListNode(x)
                    l = l.next
            return result

        def add(l1, l2):
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
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        l = add(l1, l2)
        return reverse(l)
