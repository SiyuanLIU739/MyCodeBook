public class Q733 {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if(image[sr][sc] == color){
            return image;
        }

        this.fill(image, sr, sc, color);

        return image;
    }

    public void fill(int[][] image, int sr, int sc, int color){
        int originalColor = image[sr][sc];

        image[sr][sc] = color;

        int[] dr = {0, -1, 0, 1};
        int[] dc = {1, 0, -1, 0};

        for(int i = 0; i < 4; i++){
            int r = sr + dr[i];
            int c = sc + dc[i];

            if((r < 0) || (r >= image.length) || (c < 0) || (c >= image[0].length) || (image[r][c] != originalColor)){
                continue;
            }

            this.fill(image, r, c, color);
        }
    }
}
