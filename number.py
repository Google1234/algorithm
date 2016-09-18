class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_pointer=0
        p_pointer=0
        last_p_pointer=-1
        last_s_pointer=0
        while s_pointer<len(s):
            if p_pointer<len(p) and (p[p_pointer]=='?' or p[p_pointer]==s[s_pointer]):
                p_pointer+=1
                s_pointer+=1
            elif p_pointer<len(p) and p[p_pointer]=='*':
                last_p_pointer=p_pointer+1
                last_s_pointer=s_pointer
                p_pointer+=1
            elif last_p_pointer>0:
                last_s_pointer+=1
                s_pointer=last_s_pointer
                p_pointer=last_p_pointer
            else:
                return False
        while p_pointer<len(p) and p[p_pointer]=='*':
            p_pointer+=1
        if p_pointer==len(p):
            return True
        else:
            return False




