class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp=[[False for i in range(len(s)+1)] for j in range(len(p)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            for j in range(len(s)+1):
                if p[i-1]=='*':
                    dp[i][j]=dp[i-2][j] or ((p[i-2]=='.' or p[i-2]==s[j-1])and dp[i-1][j])
                else:
                    dp[i][j]=j>0 and (p[i-1]==s[j-1] or p[i-1]=='.') and dp[i-1][j-1]
        return dp[len(p)][len(s)]

a=Solution()
print a.isMatch("aa","a*")