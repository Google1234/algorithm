class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        if n==0:
            return True
        if n%2!=0:
            return False
        stack=[' ' for i in xrange(n+1)]
        length=0
        for i in xrange(len(s)):
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                length += 1
                stack[length]=s[i]
            elif (s[i]==")" and stack[length]=="(") or (s[i]=="]" and stack[length]=="[") or (s[i]=="}" and stack[length]=="{"):
                length-=1
            else:
                return False
        if length==0:
            return True
        else:
            return False
