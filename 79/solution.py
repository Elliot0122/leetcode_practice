class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, word, posx, posy, row, col):
            if len(word) == 0:
                return True
            ans = False
            if posx != row and board[posx+1][posy] == word[0] and not ans:
                temp = board[posx+1][posy]
                board[posx+1][posy] = "."
                ans = ans or dfs(board, word[1:], posx+1, posy, row, col)
                board[posx+1][posy] = temp
            if posx != 0 and board[posx-1][posy] == word[0] and not ans:
                temp = board[posx-1][posy]
                board[posx-1][posy] = "."
                ans = ans or dfs(board, word[1:], posx-1, posy, row, col)
                board[posx-1][posy] = temp
            if posy != col and board[posx][posy+1] == word[0] and not ans:
                temp = board[posx][posy+1]
                board[posx][posy+1] = "."
                ans = ans or dfs(board, word[1:], posx, posy+1, row, col)
                board[posx][posy+1] = temp
            if posy != 0 and board[posx][posy-1] == word[0] and not ans:
                temp = board[posx][posy-1]
                board[posx][posy-1] = "."
                ans = ans or dfs(board, word[1:], posx, posy-1, row, col)
                board[posx][posy-1] = temp
            return ans
        row = len(board)
        col = len(board[0])
        ans = False
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    board[i][j] = "."
                    ans = ans or dfs(board, word[1:], i, j, row-1, col-1)
                    board[i][j] = word[0]
        return ans
