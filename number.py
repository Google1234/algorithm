class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.matrix=[[0 for i in xrange(n)] for j in xrange(m)]
        for i in xrange(m):
            self.matrix[i][0]=1
        for i in xrange(n):
            self.matrix[0][i]=1
        return self.interation(m,n)
    def interation(self,m,n):
        if m==0 or n==0:
            return 0
        if self.matrix[m-1][n-1]!=0:
            return self.matrix[m-1][n-1]
        if m==1 or n==1:
            self.matrix[m-1][n-1]=1
        else:
            self.matrix[m-1][n-1]=self.interation(m-1,n)+self.interation(m,n-1)
        return self.matrix[m-1][n-1]

s=Solution()
print s.uniquePaths(3,7)