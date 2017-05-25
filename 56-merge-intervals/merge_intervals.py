"""
34.64%
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, cmp=lambda x,y: cmp(x.start, y.start))
        result = []
        for interval in intervals:
            if not result:
                result.append(interval)
            else:
                last = result[-1]
                if interval.start > last.end:
                    result.append(interval)
                elif interval.start >= last.start and interval.end > last.end:
                    result[-1] = Interval(last.start, interval.end)
        return result