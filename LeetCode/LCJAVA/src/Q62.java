public class Q62 {
    public int uniquePaths(int m, int n) {
        double ans = 1.0;

        if(m > n){
            m = m^n;
            n = m^n;
            m = m^n;
        }

        int b = n - 1;
        for(int a = 1; a < m; a++){
            ans = ans * ((a + b)/(a * 1.0));
        }

        return (int)ans;
    }
}
