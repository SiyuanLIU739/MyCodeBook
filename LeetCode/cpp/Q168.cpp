class Solution {
public:
    string convertToTitle(int columnNumber) {
        string ans = "";

        while(columnNumber > 0){
            int mod = (columnNumber - 1) % 26 + 1;
            ans = (char)(mod - 1 + (int)'A') + ans;
            columnNumber = (columnNumber - 1) / 26;
        }

        return ans;
    }
};