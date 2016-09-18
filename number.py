class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        matrix=[[False for i in xrange(len(p)+1)] for j in xrange(len(s)+1)]
        matrix[len(s)][len(p)]=True
        j=len(p)-1
        while j>=0 and p[j]=='*':
            matrix[len(s)][j]=True
            j-=1
        while j>=0:
            matrix[len(s)][j]=False
            j-=1
        i=len(s)-1
        while i>=0:
            j = len(p) - 1
            while j>=0:
                if p[j]=='?' or p[j]==s[i]:
                    matrix[i][j]=matrix[i+1][j+1]
                elif p[j]=='*':
                    matrix[i][j]=matrix[i][j+1]|matrix[i+1][j]
                else:
                        matrix[i][j]=False
                j-=1
            i-=1
        return matrix[0][0]


