class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        pointer1=0
        pointer2=1
        while pointer2<len(tokens):
            if tokens[pointer2]=='+':
                tokens[pointer1-1]=int(tokens[pointer1-1])+int(tokens[pointer1])
                pointer1-=1
            elif tokens[pointer2]=='-':
                tokens[pointer1-1]=int(tokens[pointer1-1])-int(tokens[pointer1])
                pointer1-=1
            elif tokens[pointer2]=='*':
                tokens[pointer1-1]=int(tokens[pointer1-1])*int(tokens[pointer1])
                pointer1-=1
            elif tokens[pointer2]=='/':
                tokens[pointer1-1]=int(tokens[pointer1-1])*1.0/int(tokens[pointer1])
                pointer1-=1
            else:
                pointer1+=1
                tokens[pointer1]=tokens[pointer2]
            pointer2+=1
        return int(tokens[0])

s=Solution()
print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])