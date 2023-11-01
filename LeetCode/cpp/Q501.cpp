struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include<vector>
#include<map>
#include<queue>
#include<algorithm>

using namespace std;

class Solution {
public:
    int countValue(TreeNode* root, int val){
        if(root == nullptr){
            return 0;
        }

        int ans = 1;
        
        if(root->val != val){
            ans = 0;
        }
        
        ans += countValue(root->left, val);
        ans += countValue(root->right, val);

        return ans;
    }

    bool cmp(pair<int, int>& a, pair<int, int>& b){
        return a.second > b.second;
    }

    vector<int> findMode(TreeNode* root) {
        map<int, int> count;

        queue<TreeNode*> q;
        q.push(root);

        while(!q.empty()){
            TreeNode* rt = q.front();
            q.pop();

            if(rt->left != nullptr){
                q.push(rt->left);
            }
            if(rt->right != nullptr){
                q.push(rt->right);
            }

            int val = rt->val;
            if(count.count(val)){
                continue;
            }

            int c = countValue(rt, val);
            count[val] = c;
        }

        vector<pair<int, int>> countVector;

        for(auto& it: count){
            countVector.push_back(it);
        }

        sort(countVector.begin(), countVector.end(), cmp);

        vector<int> ans;
        int c = 0;
        for(auto& it: countVector){
            if(c == 0){
                c = it.second;
            }

            if(c == it.second){
                ans.push_back(it.first);
            }
        }

        return ans;
    }
};