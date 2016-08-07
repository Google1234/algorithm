class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        pointer=0
        while pointer<len(str):
            t=str[pointer]
            if t==' ':
                pointer+=1
            elif t=='+' or t=='-' or (ord(t)-48>=0 and ord(t)-48<=9):
                value = 0
                if t=='+':
                    posotive=1
                elif t=='-':
                    posotive=-1
                else:
                    posotive=1
                    value=ord(t)-48
                pointer += 1
                if pointer==len(str) :
                    return value
                while pointer<len(str):
                    t=ord(str[pointer])-48
                    if t>=0 and t<=9:
                        value=value*10+t
                        pointer+=1
                    else:
                        break
                if posotive*value>2147483647:
                    return 2147483647
                elif posotive*value<-2147483648:
                    return -2147483648
                else:
                    return posotive*value
            else:
                return 0
        return 0