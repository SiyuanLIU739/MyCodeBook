public class Q2849 {
    public int abs(int x){
        if(x < 0){
            return -x;
        }
        return x;
    }
    public boolean isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        int x = this.abs(sx - fx);
        int y = this.abs(sy - fy);
        return (x <= t) & (y <= t) & ((x + y >= t) | (t > 1));  
    }

}