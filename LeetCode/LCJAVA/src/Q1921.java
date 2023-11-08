import java.util.Arrays;

public class Q1921 {
    public int eliminateMaximum(int[] dist, int[] speed) {
        int ans = 0;

        double[] time = new double[dist.length];

        for(int i = 0; i < dist.length; i++){
            time[i] = (dist[i] * 1.0) / (speed[i] * 1.0);
        }

        Arrays.sort(time);

        int t = -1;

        for(int i = 0; i < time.length; i++){
            t += 1;
            
            if(time[i] > t){
                ans += 1;
            }
            else{
                break;
            }
        }

        return ans;
    }
}
