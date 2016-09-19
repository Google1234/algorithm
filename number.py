class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        pointer=len(s)-1
        while pointer>=0 and s[pointer]==' ':
            pointer-=1
        while pointer>=0 and s[pointer]!=' ':
            pointer-=1
            count+=1
        return count