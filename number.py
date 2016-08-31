class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor==0:
            return 2147483647
        flag1=flag2=1
        if dividend<0 :
            flag1=-1
            dividend=-dividend
        if divisor<0:
            flag2=-1
            divisor=-divisor

        result=0
        while dividend>=divisor:
            mul=0
            while dividend>=(divisor<<(mul+1)):
                mul+=1
            result+=(1<<mul)
            dividend-=(divisor<<mul)
        if flag1!=flag2:
            result=-result
        if (flag1==flag2 and result>2147483647) :
            result=2147483647
        if (flag1!=flag2 and result>2147483648):
            result=-2147483648
        return result




