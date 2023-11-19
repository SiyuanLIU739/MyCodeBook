import java.util.TreeSet;

/**
 * Q1887
 */
public class Q1887 {

    public int reductionOperations(int[] nums) {
        TreeSet<Integer> set = new TreeSet<>();

        for(int num: nums){
            set.add(num);
        }

        int n = 0;

        int[] sortedNums = new int[nums.length];
        while(set.size() != 0){
            int num = set.first();
            set.remove(num);

            sortedNums[n] = num;
            n += 1;

            System.out.println(num);
        }

        int ans = 0;

        for(int i = 0; i < nums.length; i++){
            ans += this.findIndex(sortedNums, nums[i], 0, n - 1);
        }

        return ans;
    }

    public int findIndex(int[] nums, int target, int l, int r){
        if(nums[l] == target){
            return l;
        }

        if(nums[r] == target){
            return r;
        }

        int mid = (l + r) >> 1;

        if(nums[mid] == target){
            return mid;
        }

        if(nums[mid] > target){
            return this.findIndex(nums, target, l, mid);
        }

        return this.findIndex(nums, target, mid + 1, r);
    }
}