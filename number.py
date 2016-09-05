class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0:
            return []
        s=['' for i in xrange(len(digits))]
        count=[0 for i in xrange(len(digits))]
        begin=['','','a','d','g','j','m','p','t','w']
        max_count=[3 for i in xrange(len(digits))]
        result=[]
        for i in xrange(len(digits)):
            if digits[i]=='9' or digits[i]=='7':
                max_count[i]=4
        deepth=0
        while deepth>=0:
            if deepth<len(digits)-1:
                if count[deepth]<max_count[deepth]:
                    s[deepth] = chr(ord(begin[int(digits[deepth])]) + count[deepth])
                    count[deepth]+=1
                    deepth+=1
                else:
                    count[deepth]=0
                    deepth-=1
            else:
                if count[deepth]<max_count[deepth]:
                    s[deepth] = chr(ord(begin[int(digits[deepth])]) + count[deepth])
                    count[deepth]+=1
                    result.append( ''.join(s))
                else:
                    count[deepth]=0
                    deepth-=1
        return result

