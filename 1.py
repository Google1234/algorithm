class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums=nums
        self.index=[i for i in range(len(nums))]
        self.quick_sort(0,len(nums)-1)
        pointer1=0
        pointer2=len(nums)-1
        while pointer1<pointer2:
            if nums[self.index[pointer1]]+nums[self.index[pointer2]]>target:
                pointer2-=1
            else:
                if nums[self.index[pointer1]]+nums[self.index[pointer2]]<target:
                    pointer1+=1
                else:
                    return [self.index[pointer1],self.index[pointer2]]

    def quick_sort(self,left,right):
        if left!=right:
            mid=(left+right)/2
            self.quick_sort(left,mid)
            self.quick_sort(mid+1,right)
            pointer1=left
            pointer2=mid+1
            pointer=left
            buff=[0 for i in range(len(self.index))]
            while pointer1<=mid and pointer2<=right:
                if self.nums[self.index[pointer1]]>=self.nums[self.index[pointer2]]:
                    buff[pointer]=self.index[pointer2]
                    pointer2+=1
                else:
                    buff[pointer]=self.index[pointer1]
                    pointer1+=1
                pointer+=1
            if pointer1>mid:
                while pointer2<=right:
                    buff[pointer]=self.index[pointer2]
                    pointer2+=1
                    pointer+=1
            else:
                while pointer1<=mid:
                    buff[pointer]=self.index[pointer1]
                    pointer1+=1
                    pointer+=1
            t=left
            while t<=right:
                self.index[t]=buff[t]
                t+=1
a=Solution()
print a.twoSum([3,2,4],6)