class MountainArray{
    int[] arr;

    public MountainArray(int[] arr){
        this.arr = arr;
    }

    public int get(int k){
        return arr[k];
    }

    public int length(){
        return arr.length;
    }
}

public class Q1095 {
    public static int findInMountainArray(int target, MountainArray mountainArr) {
        int peak = findPeak(mountainArr, 1, mountainArr.length() - 2);
        
        int ans = findLeft(mountainArr, 0, peak, target);

        if(ans == -1){
            return findRight(mountainArr, peak + 1, mountainArr.length() - 1, target);
        }
        return ans;
    }

    public static int findLeft(MountainArray arr, int l, int r, int target){
        if(l == r){
            if(arr.get(l) == target){
                return l;
            }
            return -1;
        }

        int mid = (l + r) / 2;
        int arrMid = arr.get(mid);
        
        if(arrMid == target){
            return mid;
        }

        if(arrMid > target){
            return findLeft(arr, l, mid, target);
        }

        return findLeft(arr, mid + 1, r, target);
    }

    public static int findRight(MountainArray arr, int l, int r, int target){
        if(l == r){
            if(arr.get(l) == target){
                return l;
            }
            return -1;
        }

        int mid = (l + r) / 2;
        int arrMid = arr.get(mid);
        
        if(arrMid == target){
            return mid;
        }

        if(arrMid < target){
            return findRight(arr, l, mid, target);
        }

        return findRight(arr, mid + 1, r, target);
    }

    public static int findPeak(MountainArray arr, int l, int r){
        int mid = (l + r) / 2;
        int arrMid = arr.get(mid);
        int arrMid1 = arr.get(mid + 1);

        if((arrMid > arr.get(mid - 1)) && (arrMid > arrMid1)){
            return mid;
        }

        if(arrMid > arrMid1){
            return findPeak(arr, l, mid - 1);
        }

        return findPeak(arr, mid + 1, r);
    }

    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5,3,1};
        MountainArray mArr = new MountainArray(arr);
        System.out.println(findInMountainArray(3 ,mArr));
    }
}
