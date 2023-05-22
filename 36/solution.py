class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            exist_row = {}
            exist_col = {}
            for j in range(9):
                if board[i][j]!= "." and board[i][j] in exist_row:
                    return False
                else:
                    exist_row[board[i][j]] = 1
                if board[j][i]!= "." and board[j][i] in exist_col:
                    return False
                else:
                    exist_col[board[j][i]] = 1
            
        box = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
        for i in box:
            exist = {}
            for j in range(3):
                for k in range(3):
                    if board[i[0]+j][i[1]+k] != "." and board[i[0]+j][i[1]+k] in exist:
                        print("C")
                        return False
                    else:
                        exist[board[i[0]+j][i[1]+k]] = 1
        return True
