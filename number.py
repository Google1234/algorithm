class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result=[-1,-1]
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)/2
            if nums[mid]==target:
                right1=right
                mid1=mid
                right=mid
                while left<right:
                    mid=(left+right)/2
                    if target<=nums[mid]:
                        right=mid
                    else:
                        left=mid+1
                result[0]=left
                left=mid1
                right=right1
                while left<right:
                    mid=(left+right+1)/2
                    if target<nums[mid]:
                        right=mid-1
                    else:
                        left=mid
                result[1]=right
                return result
            elif target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
        return result