class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result=[]
        s=[]
        for i in xrange(len(digits)):
            s.append(chr((ord(digits[i])-ord('2'))*3+ord('a')))
        length=[3,3,3,3,3,3,3,4]
        for i in xrange(len(digits)):
            for j in xrange(length[ord(digits[i])-ord('2')]):
                s[i]=chr((ord(digits[i])-ord('2'))*3+ord('a')+j)
                result.append(''.join(s))
        return result
s=Solution()
print s.letterCombinations("239")