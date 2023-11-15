import java.util.Arrays;

public class Q1846 {
    public int maximumElementAfterDecrementingAndRearranging(int[] arr) {
        Arrays.sort(arr);

        int currI = 2;
        
        arr[0] = 1;
        for(int i = 1; i < arr.length; i++){
            if(arr[i] > currI){
                arr[i] = currI;S
                currI += 1;
            }
            else{
                currI = arr[i] + 1;
            }
        }

        return arr[arr.length - 1];
    }
    
}
