#include <cstdio>
#include <math.h>
#include <cstring>

using namespace std;

const int nums_length = 100005;

int binarySearch(int* nums, int l, int r, int target){
    if(nums[l] >= target){
        return l;
    }

    if(l == r){
        return l;
    }

    int mid = (l + r) >> 1;

    if(nums[mid + 1] < target){
        return binarySearch(nums, mid + 1, r, target);
    }

    if(nums[mid + 1] == target){
        if(nums[mid] == target){
            return binarySearch(nums, l, mid, target);
        }
        return mid + 1;
    }

    if(nums[mid] < target){
        return mid + 1;
    }

    return binarySearch(nums, l, mid, target);
}

int binarySearch2(int* nums, int l, int r, int target){
    if(nums[r] >= target){
        return r;
    }

    if(l == r){
        return l;
    }

    int mid = (l + r) >> 1;

    if(nums[mid + 1] >= target){
        return binarySearch2(nums, mid + 1, r, target);
    }

    if(nums[mid] >= target){
        return mid;
    }

    return binarySearch2(nums, l, mid, target);
}

int maximumScore(int* nums, int numsSize, int k){
    int minNum[nums_length];
    memset(minNum, 0, sizeof(minNum));
    minNum[k] = nums[k];

    int i;
    for(i = k - 1; i >= 0; i--){
        minNum[i] = min(minNum[i + 1], nums[i]);
    }
    for(i = k + 1; i < numsSize; i++){
        minNum[i] = min(minNum[i - 1], nums[i]);
    }

    int ans = -1, j;
    for(j = k; j < numsSize; j++){
        if(minNum[j] == minNum[j + 1]){
            continue;
        }
        i = binarySearch(minNum, 0, k, minNum[j]);
        ans = max(ans, minNum[j] * (j - i + 1));
    }
    for(i = 0; i <= k; i++){
        if(minNum[i] == (i > 0 ? minNum[i - 1]: 0)){
            continue;
        }
        j = binarySearch2(minNum, k, numsSize - 1, minNum[i]);
        ans = max(ans, minNum[i] * (j - i + 1));
    }

    return ans;
}

int main(){
    int nums1[6] = {1,4,3,7,4,5};
    int k = 3, s = 6;
    printf("%d", maximumScore(nums1, s, k));
}