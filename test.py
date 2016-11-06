class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for num in nums:
            if num in dic.keys():
                dic[num]+=1
            else:
                dic[num]=1
        for num in nums:
            if dic[num]==1:
                return num
a=Solution()
print a.singleNumber([1])