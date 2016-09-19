class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        count=0
        left=0
        right=0
        while True:
            most_right=right
            count += 1
            while left<=right:
                if left+nums[left]>most_right:
                    most_right=left+nums[left]
                    if most_right>=len(nums)-1:
                        return count
                left+=1
            left=right+1
            right=most_right