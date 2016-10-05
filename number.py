class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        self.m=len(obstacleGrid)
        self.n=len(obstacleGrid[0])
        self.matrix=[[-1 for i in xrange(self.n)] for j in xrange(self.m)]
        self.matrix[self.m-1][self.n-1]=1
        self.obstacleGrid=obstacleGrid
        if obstacleGrid[0][0]==1:
            return 0
        return self.interation(0,0)

    def interation(self,m,n):
        if self.matrix[m][n]!=-1:
            return self.matrix[m][n]
        if m+1<self.m and self.obstacleGrid[m+1][n]==0:
            if n+1<self.n and self.obstacleGrid[m][n+1]==0:
                self.matrix[m][n]=self.interation(m+1,n)+self.interation(m,n+1)
            else:
                self.matrix[m][n] = self.interation(m + 1, n)
        else:
            if n+1<self.n and self.obstacleGrid[m][n+1]==0:
                self.matrix[m][n]=self.interation(m,n+1)
            else:
                self.matrix[m][n] = 0
        return self.matrix[m][n]
s=Solution()
print s.uniquePaths(3,7)