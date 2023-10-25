#include<cstdio>
#include<vector>
#include<cstring>
#include<queue>

using namespace std;

typedef struct maxQueue{
    priority_queue<int> Q, D;

    void push(int x){
        Q.push(x);
    }

    void erase(int x){
        D.push(x);
    }

    int top(){
        while(!D.empty() && (Q.top() == D.top())){
            Q.pop();
            D.pop();
        }
        return Q.empty()? -2147483647: Q.top();
    }
} maxQueue;

int constrainedSubsetSum(vector<int>& nums, int k) {
    int ans = -1000000;
    int f[100005];
    f[0] = 0;
    maxQueue q;
    q.push(f[0]);

    int i = 0;
    for(auto num = nums.cbegin(); num != nums.cend(); num++){
        i++;
        f[i] = q.top() + *num;

        q.push(f[i]);
        if(i - k > 0){
            q.erase(f[i - k]);
        }
        
        ans = max(ans, f[i]);
    }

    return ans;
}

int max(int a, int b){
    if(a > b){
        return a;
    }
    return b;
}

int main(){
    int nums[5] = {10,2,-10,5,20};
    vector<int> num;
    for(int i = 0; i < 5; i++){
        num.push_back(nums[i]);
    }
    int k = 2;
    printf("%d", constrainedSubsetSum(num, k));
}