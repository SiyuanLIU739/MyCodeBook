import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public class Q119{
    public static List<Integer> getRow(int rowIndex) {
        ArrayList<Integer> row = new ArrayList<>();

        for(int i = 0; i <= rowIndex; i++){
            row.add(getComb(i, rowIndex));
        }

        return row;
    }

    public static int getComb(int i, int n){
        int x = n - i;
        if(x < i){
            x = x^i;
            i = x^i;
            x = x^i;
        }

        BigInteger ith = getMulti(1, i);
        BigInteger nx = getMulti(x+1, n);

        int ans = nx.divide(ith).intValue();

        return ans;
    }

    public static BigInteger getMulti(int x, int n){
        BigInteger ans = new BigInteger("1");

        for(int i = x; i <= n; i++){
            String t = String.valueOf(i);
            ans = ans.multiply(new BigInteger(t));
        }

        return ans;
    }

    public static void main(String[] args) {
        System.out.println(getRow(33));
    }
}