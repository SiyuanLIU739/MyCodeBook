public class Q161 {
    public boolean isOneEditDistance(String s, String t) {
        if(this.abs(s.length() - t.length()) > 1){
            return false;
        }

        boolean changed = false;

        // remove condition
        if(this.abs(s.length() - t.length()) == 1){
            if(s.length() > t.length()){
                String m = s;
                s = t;
                t = m;
            }

            for(int i = 0; i < s.length(); i++){
                if(s.charAt(i) == t.charAt(i)){
                    continue;
                }

                if(changed == false){
                    changed = true;
                    t = t.substring(0, i).concat(t.substring(i + 1));
                    System.out.println(t);
                    i--;
                }
                else{
                    return false;
                }
            }

            return true;
        }

        // replace condition
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == t.charAt(i)){
                continue;
            }

            if(changed == false){
                changed = true;
                continue;
            }

            return false;
        }

        return (changed == true);
    }

    public int abs(int x){
        if(x < 0){
            return -x;
        }
        return x;
    }

    public static void main(String[] args) {
        String s = "ab";
        String t = "abc";

        Q161 sol = new Q161();

        System.out.println(sol.isOneEditDistance(s, t));
    }
}
