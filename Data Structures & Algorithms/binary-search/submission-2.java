public class Solution {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length;

        while (l < r) {
            int m = l + ((r - l) / 2);
            if (nums[m] > target) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return (l > 0 && nums[r - 1] == target) ? r - 1 : -1;
    }
}