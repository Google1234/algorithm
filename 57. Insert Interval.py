class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result=[]
        pointer=0
        while pointer<len(intervals) and intervals[pointer].end<newInterval.start:
            pointer+=1
        result+=intervals[:pointer]
        if pointer<len(intervals) and intervals[pointer].start<newInterval.start:
            newInterval.start=intervals[pointer].start

        while pointer<len(intervals) and intervals[pointer].end<newInterval.end:
            pointer+=1
        if pointer<len(intervals) and intervals[pointer].start<=newInterval.end:
            newInterval.end=intervals[pointer].end
            pointer+=1
        result+=[newInterval]
        result+=intervals[pointer:]
        return  result
