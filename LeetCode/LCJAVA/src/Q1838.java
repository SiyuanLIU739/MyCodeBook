import java.util.Arrays;

/**
 * Q1838
 */
public class Q1838 {

    public int maxFrequency(int[] nums, int k) {
        Arrays.sort(nums);

        long[] sum = new long[nums.length];

        sum[0] = nums[0];

        for(int i = 1; i < nums.length; i++){
            sum[i] = sum[i - 1] + nums[i];
        }

        return this.getFrequency(nums, sum, k, 1l, (long)nums.length);
    }

    public int getFrequency(int[] nums, long[] sum, int k, long l, long r){
        if(!this.checkLength(nums, sum, k, l)){
            return (int)l - 1;
        }
        if(this.checkLength(nums, sum, k, r)){
            return (int)r;
        }

        long mid = (l + r) >> 1;

        if(this.checkLength(nums, sum, k, mid)){
            return this.getFrequency(nums, sum, k, mid + 1, r);
        }
        return this.getFrequency(nums, sum, k, l, mid);
    }

    public boolean checkLength(int[] nums, long[] sum, int k, long length){
        if(nums[(int)length - 1] * length - sum[(int)length - 1] <= k){
            return true;
        }

        for(int i = (int)length; i < nums.length; i++){
            if(nums[i] * length - sum[i] + sum[i - (int)length] <= k){
                return true;
            }
        }
        
        return false;
    }
}