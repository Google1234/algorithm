class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board)!=9 or len(board[0])!=9:
            return False
        for i in xrange(9):
            dict={}
            for j in xrange(9):
                if board[i][j]!='.':
                    if dict.has_key(board[i][j]):
                        return False
                    else:
                        dict[board[i][j]]=0
        for i in xrange(9):
            dict = {}
            for j in xrange(9):
                if board[j][i] != '.':
                    if dict.has_key(board[j][i]):
                        return False
                    else:
                        dict[board[j][i]] = 0
        for count in xrange(9):
            dict={}
            for j in xrange(9):
                if board[3*(count/3)+j/3][3*(count%3)+j%3]!='.':
                    if dict.has_key(board[3*(count/3)+j/3][3*(count%3)+j%3]):
                        return False
                    else:
                        dict[board[3*(count/3)+j/3][3*(count%3)+j%3]] = 0
        return True