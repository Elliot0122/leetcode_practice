class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        path = [0]*len(grid[0])

        for i in range(len(grid)):
            path[0] += grid[i][0]
            for j in range(1, len(grid[0])):
                if i == 0:
                    path[j] = grid[i][j] + path[j-1]
                path[j] = grid[i][j] + min(path[j-1], path[j])

        return path[-1]
