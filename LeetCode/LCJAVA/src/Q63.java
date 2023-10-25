class Q63{
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;

        int[][] f = new int[m][n];
        f[0][0] = (obstacleGrid[0][0] == 1 ? 0: 1);

        for(int i = 1; i < m; i++){
            f[i][0] = (obstacleGrid[i][0] == 1 ? 0: f[i - 1][0]);
        }
        for(int j = 1; j < n; j++){
            f[0][j] = (obstacleGrid[0][j] == 1 ? 0: f[0][j - 1]);
        }

        for(int i = 1; i < m; i++){
            for(int j = 1; j < n; j++){
                f[i][j] = (obstacleGrid[i][j] == 1 ? 0: f[i][j - 1] + f[i - 1][j]);
            }
        }

        return f[m - 1][n - 1];
    }

}