import java.util.HashSet;
import java.util.TreeSet;

class Q1845{
    TreeSet<Integer> s;
    
    public Q1845(int n) {
        this.s = new TreeSet<>();
        
        for(int i = 1; i <= n; i++){
            s.add(i);
        }
    }
    
    public int reserve() {
        int t = s.first();
        
        s.remove(t);

        return t;
    }
    
    public void unreserve(int seatNumber) {
        s.add(seatNumber);
    }
}