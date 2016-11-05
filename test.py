class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left=0
        right=len(s)-1
        while left<=right:
            if (48<=ord(s[left])<=57 or 65<=ord(s[left])<=90 or 97<=ord(s[left])<=122)==False:
                left+=1
                continue
            if (48<=ord(s[right])<=57 or 65<=ord(s[right])<=90 or 97<=ord(s[right])<=122)==False:
                right-=1
                continue
            if (s[left]==s[right]) or (ord(s[left])>48 and ord(s[right])>48 and (ord(s[left])-ord(s[right])==32 or ord(s[left])-ord(s[right])==-32)):
                left += 1
                right -= 1
            else:
                return  False
        return True