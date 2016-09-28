class Solution(object):
    def merge(self, intervals):
        """
        :type nums: List[Interval]
        :rtype: List[Interval]
        """
        if intervals==[]:
            return []
        self.intervals=intervals
        self.sort(0,len(intervals)-1)
        result=[]
        left=0
        right=1
        while right<len(self.intervals):
            if self.intervals[left].end<self.intervals[right].start:
                result.append(self.intervals[left])
                left=right
            else:
                if self.intervals[left].end<self.intervals[right].end:
                    self.intervals[left].end=self.intervals[right].end
            right+=1
        result.append(self.intervals[left])
        return result

    def sort(self,left,right):
        if left<right:
            mid=(left+right)/2
            self.sort(left,mid)
            self.sort(mid+1,right)
            buff=[Interval() for i in xrange(right-left+1)]
            pointer1=left
            pointer2=mid+1
            pointer=0
            while pointer1<=mid and pointer2<=right:
                if self.intervals[pointer1].start<self.intervals[pointer2].start:
                    buff[pointer]=self.intervals[pointer1]
                    pointer1+=1
                else:
                    buff[pointer]=self.intervals[pointer2]
                    pointer2+=1
                pointer+=1
            while pointer1<=mid:
                buff[pointer]=self.intervals[pointer1]
                pointer1+=1
                pointer+=1
            while pointer2<=right:
                buff[pointer]=self.intervals[pointer2]
                pointer2+=1
                pointer+=1
            i=0
            while i<=right-left:
                self.intervals[left+i]=buff[i]
                i+=1