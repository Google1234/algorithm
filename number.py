class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        if length==0:
            return 0
        begin=stop=0
        pointer=0
        while True:
            while stop<length and nums[begin]==nums[stop]:
                stop+=1
            if stop==length:
                break
            nums[pointer]=nums[begin]
            pointer+=1
            begin=stop
        nums[pointer]=nums[begin]
        return pointer+1

