class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums=nums
    def divide(self,left,right):
        mid=(left+right)/2
        left1,right1,value1=self.divide(left,mid)
        left2,right2,value2=self.divide(mid,right)


        right3 = mid
        sum=self.nums[mid]
        sum_max=self.nums[mid]
        pointer = mid + 1
        while pointer<=left2:
            sum+=self.nums[pointer]
            if sum>sum_max:
                sum_max=sum
                right3=pointer
            pointer+=1
        if right3==left2:
            right3=right2
            sum_max=sum_max+value2-self.nums[left2]
        pointer=mid-1
        left3=mid
        sum=sum_max
        while pointer>=right1:
            sum+=self.nums[pointer]
            if sum>=sum_max:
                left3=pointer
                sum_max=sum_max
            pointer-=1
        if left3==right1:
            sum_max=sum_max+value1-self.nums[right1]
        if sum_max>