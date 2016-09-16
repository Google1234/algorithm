class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result=[]
        cur=[]

        pointer=0
        stack=[]

        while pointer<len(candidates):
                if target>0:
                    cur.append(candidates[pointer])
                    target-=candidates[pointer]
                    stack.append(pointer)
                else:
                    if target==0:
                        result.append([t for t in cur])
                    if len(cur)<2:
                        return result
                    target+=(cur.pop()+cur.pop())
                    stack.pop()
                    pointer=stack.pop()+1
                    while pointer<len(candidates) and candidates[pointer]==candidates[pointer-1]:
                        pointer+=1
        return result