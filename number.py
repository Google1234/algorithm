class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        t=1
        next="1"
        while True:
            if t==n:
                return next
            t+=1
            s=next+" "
            next=""
            pointer = 0
            count = 0
            while pointer<len(s):
                if pointer==0:
                    count=1
                else:
                    if s[pointer-1]==s[pointer]:
                        count+=1
                    else:
                        next+=str(count)
                        next+=s[pointer-1]
                        count=1
                pointer+=1