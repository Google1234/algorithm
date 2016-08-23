class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums)<4:
            return []
        result=[]
        nums.sort()
        for pointer1 in xrange(0,len(nums)-3):
            if nums[pointer1]>target/4:
                break
            if nums[pointer1]==nums[pointer1-1] and pointer1>0:
                continue
            pointer2=pointer1+1
            for pointer2 in xrange(pointer1+1,len(nums)-2):
                if nums[pointer2]>(target-nums[pointer1])/3:
                    break
                if nums[pointer2]==nums[pointer2-1] and pointer2>pointer1+1:
                    continue
                pointer3=pointer2+1
                pointer4=len(nums)-1
                need=target-nums[pointer1]-nums[pointer2]
                if nums[pointer3]>need/2 or nums[pointer4]<need/2:
                    continue
                while pointer3<pointer4:
                    t=nums[pointer3]+nums[pointer4]
                    if t>need:
                        before=nums[pointer4]
                        while before==nums[pointer4] and pointer4>pointer3:
                            pointer4-=1
                    elif t<need:
                        before=nums[pointer3]
                        while before==nums[pointer3] and pointer3<pointer4:
                            pointer3+=1
                    else:
                        result.append([nums[pointer1],nums[pointer2],nums[pointer3],nums[pointer4]])
                        before=nums[pointer3]
                        while before==nums[pointer3] and pointer3<pointer4:
                            pointer3+=1
                        before=nums[pointer4]
                        while before==nums[pointer4] and pointer4>pointer3:
                            pointer4-=1
        return result
