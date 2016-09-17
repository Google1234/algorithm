class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        length=len(nums)
        while i<length:
            if nums[i]<i+1 and nums[i]>0 and nums[i]!=nums[nums[i]-1]:
                t=nums[nums[i] - 1]
                nums[nums[i]-1]=nums[i]
                nums[i]=t
            else:
                i+=1
        i=0
        while i<length:
            if nums[i]==i+1:
                i+=1
            else:
                return i+1
        return length+1