class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return ''
        s=list(s)
        l=len(s)
        for i in range((l+1)/2):
            t=s[i]
            s[i]=s[l-1-i]
            s[l-1-i]=t
        return ''.join(s)
