class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one=0
        two=0
        three=0
        four=0
        for num in nums:
            three|=(two&one)
            two|=(one&num)
            one^=num
            four=three&(~one)
            one&=(~four)
            two&=(~four)
            three&=(~four)
        return one

s=Solution()
print s.singleNumber([2,3,4,1,2,3,4,2,3,4,4,3,2,1,1,1,5])