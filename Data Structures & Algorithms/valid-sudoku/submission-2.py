from collections import Counter
class Solution:
    def isValidSudoku(self, board: list[list[str]]):
        rows = len(board)
        cols = len(board[0])
        
        def checkValid(l: list):
            num = [i for i in range(2,10)]
            if l == [] or l == ['.']*9:
                return True
            hm = Counter(l)
            hm['.'] = 0
            for x in hm.values():
                if x in num:
                    return False
            return True
            
        for i in range(rows):
            r = board[i]
            c = [row[i] for row in board]
            for j in range(0,cols,3):
                if (i + j)%3 == 0:
                    box = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                    if checkValid(box) == False:
                        return False
                else:
                    box = []
            
            thelists = [r,c]
            for l in thelists:
                if not checkValid(l):
                    return False
            
        return True       

