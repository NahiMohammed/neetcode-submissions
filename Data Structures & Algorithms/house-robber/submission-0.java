class Solution {
    public int rob(int[] nums) {
        return Math.max(helper(nums,0),helper(nums,1));

        
    }
    private int helper(int[] nums,int i){
        if(i>=nums.length){
            return 0;
        }
        return Math.max(nums[i]+helper(nums,i+2),helper(nums,i+1));

    }
}
