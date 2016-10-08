class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates==[]:
            return []
        self.result=[]
        self.stop=len(candidates)
        self.candiates=candidates
        self.candiates.sort()
        self.stack=[]
        self.backtract(0,target)
        return self.result

    def backtract(self,start,target):
        if target==0:
            self.result.append([i for i in self.stack])
        else:
            for pointer in range(start,self.stop):
                if self.candiates[pointer]>target:
                    break
                else:
                    if pointer==start or self.candiates[pointer]!=self.candiates[pointer-1]:
                        self.stack.append(self.candiates[pointer])
                        self.backtract(pointer,target-self.candiates[pointer])
                        self.stack.pop()
s=Solution()
print s.combinationSum([2,3,6,7]
,7)
