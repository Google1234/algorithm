class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)/2
            if nums[mid]==target:
                return mid
            else:
                if nums[mid]>=nums[left]:
                    if target>=nums[left] and target<nums[mid]:
                        right=mid
                    else:
                        left=mid+1
                else:
                    if target>=nums[left] or target<nums[mid]:
                        right=mid
                    else:
                        left=mid+1
        return -1