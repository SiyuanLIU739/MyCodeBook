

using namespace std;

int max(int a, int b){
    if(a > b){
        return a;
    }
    return b;
}

void swap(int* a, int* b){
    *a = *a ^ *b;
    *b = *a ^ *b;
    *a = *a ^ *b;
}

int getWinner(int* arr, int arrSize, int k) {
    int n = arrSize;

    if(k >= (n - 1)){
        int nMax = arr[0];

        for(int i = 1; i < n; i++){
            nMax = max(arr[i], nMax);
        }

        return nMax;
    }

    int win = 0;
    int cur = 1;

    while(win < k){
        if(arr[0] > arr[cur]){
            win += 1;
        }

        else{
            win = 1;
            swap(&arr[0], &arr[cur]);
        }

        cur = cur % (n - 1) + 1;
    }

    return arr[0];
}