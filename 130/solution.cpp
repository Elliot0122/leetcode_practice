class Solution {
public:
    void dfs(vector<vector<char>>& board, vector<vector<bool>>& position_not_flip, int x, int y, int row, int col){
        if(x!=0){
            if(board[x-1][y] == 'O' && position_not_flip[x-1][y] == false){
                position_not_flip[x-1][y] = true;
                dfs(board, position_not_flip, x-1, y, row, col);
            }
        }
        if(x!=row-1){
            if(board[x+1][y] == 'O' && position_not_flip[x+1][y] == false){
                position_not_flip[x+1][y] = true;
                dfs(board, position_not_flip, x+1, y, row, col);
            }
        }
        if(y!=0){
            if(board[x][y-1] == 'O' && position_not_flip[x][y-1] == false){
                position_not_flip[x][y-1] = true;
                dfs(board, position_not_flip, x, y-1, row, col);
            }
        }
        if(y!=col-1){
            if(board[x][y+1] == 'O' && position_not_flip[x][y+1] == false){
                position_not_flip[x][y+1] = true;
                dfs(board, position_not_flip, x, y+1, row, col);
            }
        }
    }
    void solve(vector<vector<char>>& board) {
        int row = board.size(), col = board[0].size();
        if(row <= 2 || col <= 2)
            return;
        vector<vector<bool>> position_not_flip;
        for(int i=0; i<row; i++){
            vector<bool> temp(col, false);
            position_not_flip.push_back(temp);
        }
        for(int i=0; i<row; i++){
            if(board[i][0] == 'O'){
                position_not_flip[i][0] = true;
                dfs(board, position_not_flip, i, 0, row, col);
            }
            if(board[i][col-1] == 'O'){
                position_not_flip[i][col-1] = true;
                dfs(board, position_not_flip, i, col-1, row, col);
            }
        }
        for(int i=0; i<col; i++){
            if(board[0][i] == 'O'){
                position_not_flip[0][i] = true;
                dfs(board, position_not_flip, 0, i, row, col);
            }
            if(board[row-1][i] == 'O'){
                position_not_flip[row-1][i] = true;
                dfs(board, position_not_flip, row-1, i, row, col);
            }
        }
        for(int i=0; i<row; i++){
            for(int j=0; j<col; j++){
                if(position_not_flip[i][j] == false)
                    board[i][j] = 'X';
            }
        }
            
    }
};
