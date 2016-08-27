class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
            return []
        self.resilt=[]
        self.generate(n,n,"")
        return self.resilt
    def generate(self,left_remain,right_remain,current):
        if right_remain==0:
            self.resilt.append(current)
        if left_remain>0:
             self.generate(left_remain-1,right_remain,current+"(")
        if right_remain>left_remain:
             self.generate(left_remain,right_remain-1,current+")")
