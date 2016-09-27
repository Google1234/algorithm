class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        left=0
        right=0
        most_right=right
        while True:
            for i in xrange(left,right+1):
                if i+nums[i]>=most_right:
                    most_right=i+nums[i]
                    if most_right>=len(nums)-1:
                        return True
            if most_right==right:
                return False
            else:
                left = right
                right=most_right