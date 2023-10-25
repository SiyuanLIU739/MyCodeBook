import java.util.HashMap;

public class Q2742 {
    int maxCost = 6 * 100000000;
    HashMap<Integer, Integer> fSearched = new HashMap<>();
    public int paintWalls(int[] cost, int[] time) {
        int timeAvailable = 0;
        for(int i = 0; i < time.length; i++){
            timeAvailable += time[i];
        }

        return this.f(time.length, timeAvailable, cost, time);
    }

    public int f(int i, int timeAvailable, int[] cost, int[] time){
        if(timeAvailable < 0){
            return this.maxCost;
        }

        if(i == 0){
            return 0;
        }

        int key = timeAvailable * 1000 + i;
        if(this.fSearched.containsKey(key)){
            return fSearched.get(key);
        }

        int value = this.min(f(i - 1, timeAvailable - time[i - 1] - 1, cost, time), f(i - 1, timeAvailable, cost, time) + cost[i - 1]);
        this.fSearched.put(key, value);

        return value;
    }

    public int min(int a, int b){
        if(a > b){
            return b;
        }
        return a;
    }

    public static void main(String[] args) {
        Q2742 sol = new Q2742();
        int[] cost = {1,2,3,2};
        int[] time = {1,2,3,2};
        System.out.println(sol.paintWalls(cost, time));
    }
}

