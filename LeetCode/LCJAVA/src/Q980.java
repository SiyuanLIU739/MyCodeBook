public class Q980 {
    int ans = 0;
    int targetBox;
    boolean[][] passed;
    int[] steps_x = {-1, 0, 1, 0};
    int[] steps_y = {0, -1, 0, 1};
    int end_x, end_y;
    int m, n;

    public int uniquePathsIII(int[][] grid) {
        this.m = grid.length;
        this.n = grid[0].length;
        this.targetBox = m * n;
        this.passed = new boolean[m][n];

        int s = 0, t = 0;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == 1){
                    s = i; t = j;
                }
                else if(grid[i][j] == 2){
                    this.end_x = i;
                    this.end_y = j;
                }
                else if(grid[i][j] == -1){
                    this.targetBox -= 1;
                }
            }
        }

        this.search(grid, s, t, 1);
        
        return this.ans;
    }

    public void search(int[][] grid, int s, int t, int boxes){
        if((s == this.end_x) && (t == this.end_y)){
            if(boxes == this.targetBox - 1){
                this.ans += 1;
            }
            return;
        }

        this.passed[s][t] = true;

        for(int i = 0; i < 4; i++){
            int x = s + this.steps_x[i];
            int y = t + this.steps_y[i];

            if(x < 0 || y < 0 || x == this.m || y == this.n){
                continue;
            }

            if(this.passed[x][y]){
                continue;
            }

            if(grid[x][y] == -1){
                continue;
            }

            this.search(grid, x, y, boxes + 1);
        }

        this.passed[s][t] = false;
    }
}
