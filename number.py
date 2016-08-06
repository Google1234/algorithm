class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse=0
        if x<0:
            t=-1
            x=x*t
        else:
            t=1
        while x!=0:
            reverse=((x%10)+reverse*10)
            if reverse>2147483648:
                return 0
            x=x/10
        return reverse*t