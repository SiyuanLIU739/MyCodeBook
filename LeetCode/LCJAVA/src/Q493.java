import java.util.HashMap;

public class Q493{
    public int reversePairs(int[] nums) {
        HashMap<Integer, Integer> coeff = new HashMap<>();

        int ans = 0;
        int target, coefficient;

        for(int num: nums){
            target = getTarget(num);

            if(coeff.containsKey(target)){
                coefficient = coeff.get(target);
                coefficient += 1;
                coeff.put(target, coefficient);
            }
            else{
                coeff.put(target, 1);
            }
        }

        for(int i = nums.length - 1; i >= 0; i--){
            target = getTarget(nums[i]);
            coefficient = coeff.get(target);
            if(coefficient == 1){
                coeff.remove(target);
            }
            else{
                coefficient -= 1;
                coeff.put(target, coefficient);
            }

            for(int j: coeff.keySet()){
                if(nums[i] <= j){
                    ans += coeff.get(j);
                }
            }
        }

        return ans;
    }

    public static int getTarget(int x){
        if(x > 0){
            return (x - 1) / 2;
        }
        return x / 2 - 1;
    }
}