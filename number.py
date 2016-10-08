class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board)==9 and len(board[0])==9:
            self.board=[list(board[i]) for i in xrange(9)]
            self.backtrack(0)
            for i in xrange(9):
                board[i]=''.join(self.board[i])

    def backtrack(self,i):
        if i>=81:
            return True
        else:
            x=i/9
            y=i%9
            if self.board[x][y]!='.':
                if self.valid(x,y)==True:
                    return self.backtrack(i+1)
                else:
                    return False
            else:
                for num in "123456789":
                    self.board[x][y]=num
                    if self.valid(x,y)==True and self.backtrack(i+1)==True:
                        return True
                    self.board[x][y]='.'
                return False

    def valid(self,x,y):
        for i in xrange(9):
                if i!=y and self.board[x][i]==self.board[x][y]:
                    return False
        for i in xrange(9):
                if i!=x and self.board[i][y] == self.board[x][y]:
                    return False
        for i in xrange((x/3)*3,(x/3+1)*3):
            for j in xrange((y/3)*3,(y/3+1)*3):
                if (i!=x and j!=y) and self.board[i][j]==self.board[x][y]:
                    return False
        return True
s=Solution()
s.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])