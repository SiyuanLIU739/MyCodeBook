public class Q402 {
    public String modify(String s){
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) != '0'){
                return s.substring(i);
            }
        }

        return "0";
    }

    public String removeKdigits(String num, int k) {
        if(k == num.length()){
            return "0";
        }

        StringBuilder str = new StringBuilder("");

        for(int i = 0; i < num.length(); i++){
            while((k > 0) && (str.length() != 0) && (str.charAt(str.length() - 1) > num.charAt(i))){
                str.deleteCharAt(str.length() - 1);
                k--;
            }
            if(k == 0){
                str.append(num.substring(i));

                return this.modify(str.toString());
            }
            str.append(num.charAt(i));
        }

        String ans = str.toString();

        return this.modify(ans.substring(0, ans.length() - k));
    }
}
