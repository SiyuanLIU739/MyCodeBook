public class Q1220 {
    public int countVowelPermutation(int n) {
        int[][] f = new int[n][5];

        for(int i = 0; i < 5; i++){
            f[1][i] = 1;
        }

        for(int i = 2; i <= n; i++){
            f[i][0] = f[i - 1][1] + f[i - 1][2] + f[i - 1][4];
            f[i][1] = f[i - 1][0] + f[i - 1][2];
            f[i][2] = f[i - 1][1] + f[i - 1][3];
            f[i][3] = f[i - 1][2];
            f[i][4] = f[i - 1][2] + f[i - 1][3];
        }

        int ans = 0;
        for(int i = 0; i < 5; i++){
            ans += f[n][i];
        }

        return ans;
    }
}
