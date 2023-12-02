public class Q1685{
    public int[] getSumAbsoluteDifferences(int[] nums) {
        int[] ans = new int[nums.length];

        ans[0] = 0;
        for(int i = 1; i < nums.length; i++){
            ans[0] += (nums[i] - nums[0]);
        }
        
        for(int i = 1; i < nums.length; i++){
            ans[i] = ans[i - 1] + (2 * i - nums.length) * (nums[i] - nums[i - 1]);
        }

        return ans;
    }
}