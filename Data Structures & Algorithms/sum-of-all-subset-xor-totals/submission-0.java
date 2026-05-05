class Solution {
    public int subsetXORSum(int[] nums) {
        return backtrack(nums, 0, 0);
    }

    private int backtrack(int[] nums, int index, int xor) {
        if (index == nums.length) {
            return xor;
        }

        // option 1: ne pas prendre nums[index]
        int without = backtrack(nums, index + 1, xor);

        // option 2: prendre nums[index]
        int with = backtrack(nums, index + 1, xor ^ nums[index]);

        return without + with;
    }
}