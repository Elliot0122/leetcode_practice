class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        length = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0

        path = [0]*length
        path[0] = 1

        for i in range(height):
            for j in range(length):
                if obstacleGrid[i][j] == 1:
                    path[j] = 0
                else:
                    if j > 0:
                        path[j] += path[j-1]

        return path[-1]
