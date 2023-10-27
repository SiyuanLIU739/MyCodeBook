public class Q5 {
    public String longestPalindrome(String s) {
        int ans = -1;
        int left = -1;
        int right = -1;

        for(int i = 0; i < s.length(); i++){
            
            // odd chars solution
            int l = i;
            int r = i;

            while((l >= 0) && (r < s.length())){
                if(s.charAt(l) == s.charAt(r)){
                    int length = r - l + 1;
                    if(length > ans){
                        ans = length;
                        left = l;
                        right = r;
                    }
                    l--; r++;
                }
                else{
                    break;
                }
            }

            // even chars solution
            l = i;
            r = i + 1;

            while((l >= 0) && (r < s.length())){
                if(s.charAt(l) == s.charAt(r)){
                    int length = r - l + 1;
                    if(length > ans){
                        ans = length;
                        left = l;
                        right = r;
                    }
                    l--; r++;
                }
                else{
                    break;
                }
            }
        }

        if(ans == -1){
            return "";
        }
        return s.substring(left, right + 1);
    }

    public static void main(String[] args) {
        Q5 sol = new Q5();
        String s = "bbad";
        System.out.println(sol.longestPalindrome(s));
    }
}