class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        t=0
        while x/(10**t)!=0:
            t+=1
        t_max=t
        t=1
        while t_max>=t:
            if ((x%(10**t))/(10**(t-1)))==((x/(10**(t_max-1))%10)):
                t+=1
                t_max-=1
            else:
                break
        if t_max<t:
            return True
        else:
            return False