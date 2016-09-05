class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        current=length-2
        while current>=0:
            if nums[current]<nums[length-1]:
                t=nums[current]
                i=current+1
                while i<length and nums[i]<=t:
                    i+=1
                nums[current]=nums[i]
                nums[i]=t
                break
            else:
                t=nums[current]
                i=current+1
                while i<length and nums[i]<t:
                    nums[i-1]=nums[i]
                    i+=1
                nums[i-1]=t
                current-=1

