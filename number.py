class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp=[[False for i in range(len(s)+1)] for j in range(len(p)+1)]
        dp[0][0]=True
        for j in range(1,len(s)+1):
            dp[0][j]=False
        if len(p)>0:
            dp[1][0]=False
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                dp[i][0]=dp[i-2][0]
            else:
                dp[i][0]=False
        for i in range(1,len(p)+1):
            for j in range(1,len(s)+1):
                if p[i-1]=='*':
                    dp[i][j]=dp[i-2][j] or ((p[i-2]=='.' or p[i-2]==s[j-1])and dp[i][j-1])
                else:
                    dp[i][j]=(p[i-1]==s[j-1] or p[i-1]=='.') and  dp[i-1][j-1]
        return dp[len(p)][len(s)]