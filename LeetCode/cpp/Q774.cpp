#include<queue>
#include<algorithm>
#include<vector>
#include<cstdio>
#include<cstring>

using namespace std;

class Solution {
public:
    double minmaxGasDist(vector<int>& stations, int k) {
        int n = 0;
        double dist[2000];

        double last = *stations.cbegin();

        for(auto i = stations.cbegin() + 1; i != stations.cend(); i++){
            double now = *i;

            dist[n] = now * 1.0 - last * 1.0;

            last = now;

            n += 1;
        }

        sort(dist, dist + n, greater<double>());

        double f[1000005];

        memset(f, 0, sizeof(f));

        for(int i = 0; i < n; i++){
            for(int j = k; j >= 0; j--){
                if(dist[i] <= f[j]){
                    f[j] = f[j];
                }
                else{
                    for(int l = 0; l <= j; l++){
                        f[j] = max(f[l], dist[i] / (j - l + 1));
                    }
                }
            }
        }

        return f[k];
    }
};