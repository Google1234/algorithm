class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        deepth=0
        LCP=strs[0]
        while deepth<len(strs[0]):
            for index in range(1,len(strs)):
                if deepth>=len(strs[index]) or strs[index][deepth]!=strs[0][deepth]:
                    return LCP[:deepth]
            deepth+=1
        return LCP
a=Solution()
print  a.longestCommonPrefix(["a"])