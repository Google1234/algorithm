class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        s_new=''
        if numRows==1:
            return s
        for i in range(numRows):
            pointer=i
            if pointer<len(s):
                s_new+=s[pointer]
            odd=0
            while True:
                if odd%2==0:
                    increase=2*(numRows-1-i)
                else:
                    increase=2*i
                if increase!=0:
                    pointer += increase
                    if pointer>=len(s):
                        break
                    s_new += s[pointer]
                odd+=1
        return s_new