class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=='0' or num2=='0':
            return '0'
        result=''
        level=0
        buff=0
        while level<(len(num1)+len(num2)-1):
            for offset in xrange(1,len(num1)+1):
                offset2=level-offset+2
                if offset2<=len(num2) and offset2>=1:
                    buff+=(ord(num1[-offset])-ord('0'))*(ord(num2[-offset2])-ord('0'))
            result=str(buff%10)+result
            buff=buff/10
            level+=1
        if buff!=0:
            result=str(buff)+result
        return result


