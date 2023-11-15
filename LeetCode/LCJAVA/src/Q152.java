import Math;

public class Q152 {
    public int maxProduct(int[] nums) {
        int last0 = -1;

        int[] f = new int[nums.length];

        f[0] = nums[0];
        int ans = nums[0];

        for(int j = 1; j < nums.length; j++){
            ans = Math.max(ans, nums[j]);

            if(nums[j] == 0){
                last0 = j + 1;
            }

            for(int i = Math.max(last0, 0); i < j; i++){
                f[i] = f[i] * nums[j];
            }

            f[j] = nums[j];
        }

        return ans;
    }
}
