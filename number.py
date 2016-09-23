class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs_list=[list(str) for str in strs]
        for i in xrange(len(strs)):
            strs_list[i].sort()
        sorted_strs=[''.join(l) for l in strs_list]
        dict={}
        result=[]
        deepth=0
        for i in xrange(len(strs)):
            if dict.has_key(sorted_strs[i]):
                result[dict[sorted_strs[i]]].append(strs[i])
            else:
                dict[sorted_strs[i]]=deepth
                deepth+=1
                result.append([strs[i]])
        return  result

s=Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])