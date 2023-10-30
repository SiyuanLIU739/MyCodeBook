#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    typedef struct OneNumber{
        int number;
        int n1s;

        OneNumber init(int n, int s){
            this->number = n;
            this->n1s = s;
            return *this;
        }

        bool operator < (const OneNumber b) const{
            if(this->n1s == b.n1s){
                return this->number < b.number;
            }
            return this->n1s < b.n1s;
        }
    }oneNumber;

    vector<int> sortByBits(vector<int>& arr) {
        vector<oneNumber> q;
        oneNumber N;
        for(auto i = arr.begin(); i != arr.end(); i++){
            int number = *i;

            int count = 0;
            for(int j = 1; (j >> 1) < number; j = (j << 1)){
                if((number & j) == j){
                    count++;
                }
            }
            q.push_back(N.init(number, count));
        }

        sort(q.begin(), q.end());

        vector<int> ans;
        for(auto i = q.begin(); i != q.end(); i++){
            N = *i;

            ans.push_back(N.number);
        }

        return ans;
    }
};