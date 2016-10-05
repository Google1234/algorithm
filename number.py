class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0 for i in xrange(n)] for j in xrange(m)]

        x=m-1
        while x>=0:
            y=n-1
            while y>=0:
                if obstacleGrid[x][y]==1:
                    dp[x][y]=0
                else:
                    if x+1<m :
                        if y+1<n:
                            dp[x][y]=dp[x+1][y]+dp[x][y+1]
                        else:
                            dp[x][y] = dp[x + 1][y]
                    else:
                        if y+1<n:
                            dp[x][y]=dp[x][y+1]
                        else:
                            dp[x][y] = 1
                y-=1
            x-=1
        return dp[0][0]
s=Solution()
print s.uniquePaths(3,7)