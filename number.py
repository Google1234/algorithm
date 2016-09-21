class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.length=len(nums)
        self.nums=nums
        self.result=[]
        self.DFS(0)
        return self.result
    def DFS(self,begin):
        if begin==self.length:
            self.result.append([n for n in self.nums])
        for i in xrange(begin,self.length):
            buff=self.nums[i]
            self.nums[i]=self.nums[begin]
            self.nums[begin]=buff
            self.DFS(begin+1)
            buff=self.nums[i]
            self.nums[i]=self.nums[begin]
            self.nums[begin]=buff
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
