class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        LCP=strs[0]
        for index in range(1,len(strs)):
            pointer1=0
            pointer2=0
            while pointer1<len(LCP) and pointer2<len(strs[index]):
                if LCP[pointer1]==strs[index][pointer2]:
                    pointer1+=1
                    pointer2+=1
                else:
                    break
            LCP=strs[index][:pointer2]
        return LCP
