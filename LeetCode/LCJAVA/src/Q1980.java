import java.util.HashSet;

public class Q1980 {
    public String intToString(int x, int n){
        StringBuilder builder = new StringBuilder();

        while(x > 0){
            if(x % 2 == 1){
                builder.append('1');
            }
            else{
                builder.append('0');
            }
            x = x >> 1;
        }

        while(builder.length() < n){
            builder.append('0');
        }

        return builder.reverse().toString();
    }

    public String findDifferentBinaryString(String[] nums) {
        HashSet<String> set = new HashSet<>();

        for(String num: nums){
            set.add(num);
        }

        int max = 1 << nums.length;

        for(int i = 0; i < max; i++){
            String strI = this.intToString(i, nums.length);
            if(set.contains(strI)){
                continue;
            }

            return strI;
        }

        return "";
    }
}
