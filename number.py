class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.s=s
        self.p=p
        self.matrix=[[None for i in xrange(len(self.p))] for j in xrange(len(self.s))]
        return self.match(0,0)
    def match(self,s_start,p_start):
        if s_start<len(self.s) and p_start<len(self.p):
            if self.matrix[s_start][p_start]==None:
                if self.p[p_start]=='?':
                    self.matrix[s_start][p_start]=self.match(s_start+1,p_start+1)
                elif self.p[p_start]=='*':
                    i=s_start
                    while i<=len(self.s) and self.match(i,p_start+1)==False:
                        i+=1
                    if i<=len(self.s):
                        self.matrix[s_start][p_start] = True
                    else:
                        self.matrix[s_start][p_start] = False
                else:
                    if self.p[p_start]==self.s[s_start]:
                        self.matrix[s_start][p_start]=self.match(s_start+1,p_start+1)
                    else:
                        self.matrix[s_start][p_start]=False
            return self.matrix[s_start][p_start]
        else:
            if s_start==len(self.s):
                while p_start<len(self.p) and self.p[p_start]=='*':
                    p_start+=1
                if p_start==len(self.p):
                    return True
                else:
                    return False
            else:
                return False