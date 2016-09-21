class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results=[[]]
        for n in nums:
            new=[]
            for result in results:
                for i in xrange(len(result)+1):
                    new.append(result[:i]+[n]+result[i:])
            results=new
        return results