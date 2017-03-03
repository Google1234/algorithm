class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p_max=[]
        n_min=[]
        p_max.append(1)
        n_min.append(1)
        global_max=nums[0]
        for num in nums:
            if num>0:
                p_max.append(max(num,p_max[-1]*num))
                n_min.append(min(num,n_min[-2]*num))
            else:
                p_max.append(max(num,n_min[-1]*num))
                n_min.append(min(num,p_max[-2]*num))
            if p_max[-1]>global_max:
                global_max=p_max[-1]
        return global_max


s=Solution()
print s.maxProduct([-4,-3,-2])