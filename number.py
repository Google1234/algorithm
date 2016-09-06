class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        s='#'+s
        not_matched_position=[0]
        max_length=0
        for pointer in xrange(1,len(s)):
            if s[pointer]==')' and s[not_matched_position[-1]]=='(':
                not_matched_position.pop()
                if pointer-not_matched_position[-1]>max_length:
                    max_length=pointer-not_matched_position[-1]
            else:
                not_matched_position.append(pointer)
        return max_length