class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length=len(nums)
        if length==0 or val==None:
            return length
        left=0
        right=length-1
        while True:
            while nums[left]!=val:
                left+=1
                if left>=right:
                    if nums[right]==val:
                        return right
                    else:
                        return right+1
            while nums[right]==val:
                right-=1
                if right<=left:
                    return left
            nums[left]=nums[right]
            left+=1
            right-=1