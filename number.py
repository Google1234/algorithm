class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums=nums
        left,right,value=self.divide(0,len(nums)-1)
        return value
    def divide(self,left,right):
            mid=(left+right)/2
            if left==mid:
                left1, right1, value1 =left,mid,self.nums[left]
            else:
                left1,right1,value1=self.divide(left,mid-1)
            if right==mid:
                left2, right2, value2=mid,right,self.nums[mid]
            else:
                left2,right2,value2=self.divide(mid+1,right)

            right3 = mid
            sum=self.nums[mid]
            sum_max=self.nums[mid]
            pointer = mid + 1
            while pointer<=right2:
                sum+=self.nums[pointer]
                if sum>=sum_max:
                    sum_max=sum
                    right3=pointer
                pointer+=1
            pointer=mid-1
            left3=mid
            sum=sum_max
            while pointer>=left1:
                sum+=self.nums[pointer]
                if sum>=sum_max:
                    left3=pointer
                    sum_max=sum
                pointer-=1

            if value1>value2:
                value=value1
                left=left1
                right=right1
            else:
                value=value2
                left=left2
                right=right2
            if sum_max>value:
                value=sum_max
                left=left3
                right=right3
            return left,right,value
s=Solution()
print s.maxSubArray([1,2,-1,-2,2,1,-2,1,4,-5,4])