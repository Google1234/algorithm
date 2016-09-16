class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        pointer=0
        stack=[]
        result=[]
        while True:
            if pointer<len(candidates) and candidates[pointer]<=target:
                target -= candidates[pointer]
                stack.append(pointer)
                pointer += 1
            else:
                if target==0:
                    result.append([candidates[i] for i in stack])
                if len(stack) == 0:
                    break
                pointer = stack.pop()
                target += candidates[pointer]
                pointer += 1
                while pointer < len(candidates) and candidates[pointer] == candidates[pointer - 1]:
                    pointer += 1
        return result