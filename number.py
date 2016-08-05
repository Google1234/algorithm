class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s)==0:
            return ''

        s_new='^'
        for a in s:
            s_new+='#'+a
        s_new+='#$'
        count=[0 for i in range(len(s_new))]

        C=R=0
        for i in range(len(s_new)-1):
            i_mirror = C - (i - C)
            if i>R:
                count[i]=0
            else:
                count[i] = min(count[i_mirror],R - i)

            while s_new[i + count[i] + 1] == s_new[i - count[i] - 1]:
                count[i] += 1
            if i+count[i]>R:
                C = i
                R = i + count[i]
        max_count=0
        pointer=0
        for i in range(len(count)):
            if count[i]>max_count:
                max_count=count[i]
                pointer=i
        longest_substring=''
        for i in s_new[pointer-max_count:pointer+max_count+1]:
            if i!='#':
                longest_substring+=i
        return longest_substring


