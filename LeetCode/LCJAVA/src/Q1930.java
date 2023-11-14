import java.util.HashSet;

class Q1930 {
    public int charToInt(char c){
        return ((int) c - (int) 'a');
    }

    public char intToChar(int a){
        return (char)(a + (int) 'a');
    }

    public int countPalindromicSubsequence(String s) {
        int[][] l = new int[s.length()][26];
        int[][] r = new int[s.length()][26];

        HashSet<String> constructed = new HashSet<>();

        l[0][this.charToInt(s.charAt(0))] = 1;
        for(int i = 1; i < s.length(); i++){
            int charInt = this.charToInt(s.charAt(i));
            for(int j = 0; j < 26; j++){
                if(j == charInt){
                    l[i][j] = l[i - 1][j] + 1;
                }
                else{
                    l[i][j] = l[i - 1][j];
                }
            }
        }

        r[s.length() - 1][this.charToInt(s.charAt(s.length() - 1))] = 1;
        for(int i = s.length() - 2; i >= 0; i--){
            int charInt = this.charToInt(s.charAt(i));
            for(int j = 0; j < 26; j++){
                if(j == charInt){
                    r[i][j] = r[i + 1][j] + 1;
                }
                else{
                    r[i][j] = r[i + 1][j];
                }
            }
        }

        StringBuilder builder = new StringBuilder();

        for(int i = 1; i < s.length() - 1; i++){
            for(int j = 0; j < 26; j++){
                if((l[i - 1][j] < 1) || (r[i + 1][j] < 1)){
                    continue;
                }

                builder.delete(0, builder.length() - 1);
                builder.append(this.intToChar(j));
                builder.append(s.charAt(i));
                builder.append(this.intToChar(j));

                constructed.add(builder.toString());
            }
        }

        return constructed.size();
    }
}