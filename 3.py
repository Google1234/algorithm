class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=right=pointer=max=0
        if len(s)==0:
            return 0
        while True:
            pointer=right
            right+=1
            if right==len(s):
                d=right-left
                if d>max:
                    max=d
                break
            while pointer>=left and s[right]!=s[pointer] :
                pointer-=1
            if pointer>=left:
                left=pointer+1
            d=right-left+1
            if d>max:
                max=d
        return max