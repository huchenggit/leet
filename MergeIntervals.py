# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals=sorted(intervals,key=lambda x:x.start)
        ret=[]
        length=len(intervals)
        for i in range(length):
            if i==length-1:
                ret.append(intervals[i])
            else:
                if intervals[i].end<intervals[i+1].start:
                    ret.append(intervals[i])
                else:
                    intervals[i+1].start=intervals[i].start
                    if intervals[i].end>intervals[i+1].end:
                        intervals[i+1].end=intervals[i].end
        return ret

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)

        return self.merge(intervals)