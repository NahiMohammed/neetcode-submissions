class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int l = 0;
        int r = nums.length - 1;
        int res[] = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 0) {
                res[l] = nums[i];
                l++;

            } else {
                res[r] = nums[i];
                r--;
            }
        }
        return res;
    }
}