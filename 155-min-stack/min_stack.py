"""
0.92%
"""

import collections

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = collections.deque()
        self.minlist = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.minlist.append(x)
        self.minlist = sorted(self.minlist)

    def pop(self):
        """
        :rtype: void
        """
        p = self.stack.pop()
        self.minlist.remove(p)
        return p

    def top(self):
        """
        :rtype: int
        """
        top = self.stack.pop()
        self.stack.append(top)
        return top

    def getMin(self):
        """
        :rtype: int
        """
        return self.minlist[0] if self.minlist else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()