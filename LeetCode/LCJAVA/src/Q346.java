public class Q346 {
    class MovingAverage {
        int[] nums;
        int size;
        int index;
        int sum;
        public MovingAverage(int size) {
            this.nums = new int[size];

            this.size = size;

            this.index = -1;

            this.sum = 0;
        }
        
        public double next(int val) {

            this.index += 1;

            int toFill = (this.index) % this.size;

            this.sum = this.sum - this.nums[toFill] + val;

            this.nums[toFill] = val;

            int a = this.index < this.size ? this.index : this.size;

            return this.sum / (a * 1.0);
        }
    }
}
