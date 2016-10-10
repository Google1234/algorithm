class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ban=set()
        self.stack=[]
        self.all=set([i for i in range(n)])
        self.count=0
        self.stop=n
        self.backtract(0)
        return self.count
    def backtract(self,n):
        if n==self.stop:
            self.count+=1
        else:
            candinate=self.all-self.ban
            for position in candinate:
                i=0
                flag=True
                for p in self.stack:
                    if p+(n-i)==position or p-(n-i)==position:
                        flag=False
                        break
                    i+=1
                if flag:
                    self.ban.add(position)
                    self.stack.append(position)
                    self.backtract(n+1)
                    self.ban.remove(position)
                    self.stack.pop()