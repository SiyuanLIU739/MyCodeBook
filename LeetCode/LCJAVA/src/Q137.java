import java.util.Arrays;

public class Q137 {
    public int singleNumber(int[] nums) {
        Arrays.sort(nums);

        for(int i = 0; i + 3 < nums.length; i += 3){
            if(nums[i] == nums[i + 2]){
                continue;
            }
            return nums[i];
        }

        return nums[nums.length - 1];
    }
}
