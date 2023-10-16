import java.util.Arrays;

public class Q2009 {
    public static int minOperations(int[] nums) {
        Arrays.sort(nums);

        int[] missingSum = new int[nums.length];
        int[] heads = new int[nums.length];
        int[] newNums = new int[nums.length];
        newNums[0] = nums[0];
        heads[0] = 0;
        int length = 1;
        int nHeads = 1;
        int k = 0;

        for(int i = 1; i < nums.length; i++){
            if(nums[i] == nums[i - 1]){
                k++;
            }
            else{
                newNums[length] = nums[i];

                if(nums[i] == (nums[i - 1] + 1)){
                    missingSum[length] = missingSum[length - 1];
                }
                else{
                    missingSum[length] = missingSum[length - 1] + nums[i] - nums[i - 1] - 1;
                    heads[nHeads] = length;
                    nHeads++;
                }

                length++;
            }
        }
        
        int ans = nums.length;
        int lastR = 0;

        for(int i = 0; i < nHeads; i++){
            int left = newNums[heads[i]];
            int right = left + nums.length - 1;

            int rIndex = find_index(newNums, lastR, length - 1, right);
            lastR = rIndex;

            int need = missingSum[rIndex] - missingSum[heads[i]];
            int available = k + length - (rIndex - heads[i] + 1);

            if(need > available){
                continue;
            }
            ans = min(ans, available);
        }

        return ans;
    }

    public static int find_index(int[] nums, int l, int r, int target){
        if(l == r){
            return l;
        }

        int mid = (l + r) / 2;

        if(nums[mid] == target){
            return mid;
        }
        if(nums[mid + 1] == target){
            return mid + 1;
        }
        if((nums[mid] < target) && (nums[mid + 1] > target)){
            return mid;
        }
        if(nums[mid + 1] < target){
            return find_index(nums, mid + 1, r, target);
        }
        if(nums[mid] > target){
            return find_index(nums, l, mid, target);
        }

        return -1;
    }

    public static int max(int a, int b){
        if(a > b){
            return a;
        }
        return b;
    }

    public static int min(int a, int b){
        if(a < b){
            return a;
        }
        return b;
    }

    public static void mergeSort(int[] nums, int l, int r){
        if(l == r){
            return;
        }

        if(l + 1 == r){
            if(nums[l] > nums[r]){
                nums[l] = nums[l] ^ nums[r];
                nums[r] = nums[l] ^ nums[r];
                nums[l] = nums[l] ^ nums[r];
            }
            return;
        }

        int mid = (l + r) / 2;
        mergeSort(nums, l, mid);
        mergeSort(nums, mid + 1, r);
 
        int s = l, t = mid + 1;
        int pos = l;
        int[] copy = new int[nums.length];
        while((s <= mid) && (t <= r)){
            if(nums[s] <= nums[t]){
                copy[pos] = nums[s];
                s++;
            }
            else{
                copy[pos] = nums[t];
                t++;
            }
            pos++;
        }
        while(s <= mid){
            copy[pos] = nums[s];
            s++;
            pos++;
        }
        while(t <= r){
            copy[pos] = nums[t];
            t++;
            pos++;
        }

        for(int i = l; i <= r; i++){
            nums[i] = copy[i];
        }
    }

    public static void main(String[] args){
        int[] nums = {1,10,100,1000};
        System.out.println(minOperations(nums));
    }
}