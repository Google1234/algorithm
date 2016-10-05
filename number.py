class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        dp=[[0 for i in xrange(n)]for j in xrange(m)]
        for x in xrange(m):
            for y in xrange(n):
                if x-1>=0:
                    if y-1>=0:
                        dp[x][y]=grid[x][y]+min(dp[x][y-1],dp[x-1][y])
                    else:
                        dp[x][y] = grid[x][y] + dp[x - 1][y]
                else:
                    if y-1>=0:
                        dp[x][y] = grid[x][y] + dp[x][y-1]
                    else:
                        dp[x][y]=grid[x][y]
        return dp[m-1][n-1]