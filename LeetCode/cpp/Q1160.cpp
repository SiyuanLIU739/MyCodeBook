#include<vector>
#include<string>

class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        int count[30];

        for(int i = 0; i < chars.length(); i++){
            count[chars[i] - 'a'] += 1;
        }

        int ans = 0;
        for(auto w = words.begin(); w != words.end(); w++){
            string word = *w;

            bool flag = 0;

            for(int i = 0; i < word.length(); i++){
                if(count[word[i] - 'a'] == 0){
                    for(int j = 0; j < i; j++){
                        count[word[j] - 'a'] += 1;
                    }
                    flag = 1;
                    break;
                }
                else{
                    count[word[i] - 'a'] -= 1;
                }
            }

            if(!flag){
                ans += word.length();
                for(int i = 0; i < word.length(); i++){
                    count[word[i] - 'a'] += 1;
                }
            }
        }


        return ans;
    }
};