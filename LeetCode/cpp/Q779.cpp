int kthG(int n, int k, bool reverse){
    if(n == 2){
        return (reverse^(!(k % 2)));
    }

    int mid = 1 << (n - 2);
    if(mid < k){
        return kthG(n - 1, k - mid, !reverse);
    }
    return kthG(n - 1, k, reverse);
}

int kthGrammar(int n, int k){
    if(n == 1){
        return 0;
    }

    if(n == 2){
        return !(k % 2);
    }

    return kthG(n, k, 0);
}