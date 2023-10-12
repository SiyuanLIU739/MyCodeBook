import java.util.HashMap;

public class Q167 {

    public static int[] twoSum(int[] nums, int target){
        int[] ans = new int[2];

        int l = 0;
        int r = nums.length - 1;

        while(l < r){
            int sum = nums[l] + nums[r];
            
            if(sum == target){
                ans[0] = l + 1;
                ans[1] = r + 1;
                break;
            }

            if(sum > target){
                r--;
            }
            else{
                l++;
            }
        }

        return ans;
    }

    public static void main(String[] args) throws Exception {
        int[] nums ={2,7,11,15};
        int target = 9;
        int[] ans = twoSum(nums, target);
        for(int i = 0; i < ans.length; i++){
            System.out.println(ans[i]);
        } 
    }
}
