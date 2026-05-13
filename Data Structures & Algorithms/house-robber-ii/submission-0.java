class Solution {

    public int rob(int[] nums) {
        int n = nums.length;

        if (n == 1) return nums[0];
        if (n == 2) return Math.max(nums[0], nums[1]);

        return Math.max(
            robRange(nums, 0, n - 2),
            robRange(nums, 1, n - 1)
        );
    }

    private int robRange(int[] nums, int l, int r) {
        int prev2 = 0;
        int prev1 = 0;

        for (int i = l; i <= r; i++) {
            int current = Math.max(prev1, nums[i] + prev2);
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
}