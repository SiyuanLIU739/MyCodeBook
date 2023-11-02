#include<cstring>
#include<algorithm>
#include<math.h>
#include<cstdio>

using namespace std;

class MaxStack {
public:
    const static int len = 100005;
    int maxTree[(len << 1) | 1];
    int value[len];
    int last[len], next[len];
    int index, end;
    int minNumber;

    MaxStack() {
        memset(maxTree, (1 << 7), sizeof(maxTree));
        memset(last, 0, sizeof(last));
        memset(next, 0, sizeof(next));
        minNumber = maxTree[0];
        index = end = 0;
    }

    void changeValue(int pos, int rt, int l, int r, int x){
        if(l == r){
            maxTree[rt] = x;
            return;
        }

        int left = rt << 1;
        int right = left | 1;

        int mid = (l + r) >> 1;

        if(pos <= mid){
            changeValue(pos, left, l, mid, x);
        }
        else{
            changeValue(pos, right, mid + 1, r, x);
        }

        maxTree[rt] = max(maxTree[left], maxTree[right]);
    }
    
    void push(int x) {
        index += 1;

        changeValue(index, 1, 1, len, x);

        value[index] = x;

        next[end] = index;
        last[index] = end;
        end = index;
    }
    
    int pop() {
        int m = value[end];

        changeValue(end, 1, 1, len, minNumber);

        end = last[end];
        next[end] = 0;

        return m;
    }
    
    int top() {
        return value[end];
    }
    
    int peekMax() {
        return maxTree[1];
    }

    int delMax(int rt, int l, int r, int target){
        if(l == r){
            maxTree[rt] = minNumber;
            return l;
        }

        int left = rt << 1;
        int right = left | 1;

        int mid = (l + r) >> 1;

        int pos;
        if(maxTree[right] == target){
            pos = delMax(right, mid + 1, r, target);
        }
        else{
            pos = delMax(left, l, mid, target);
        }

        maxTree[rt] = max(maxTree[left], maxTree[right]);

        return pos;
    }
    
    int popMax() {
        int m = maxTree[1];

        if(value[end] == maxTree[1]){
            pop();
            return m;
        }

        int pos = delMax(1, 1, len, maxTree[1]);

        int l = last[pos];
        int n = next[pos];

        next[l] = n;
        last[n] = l;

        return m;
    }


};
