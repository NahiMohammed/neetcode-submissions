class Solution {
    int[] memo ;
    public int rob(int[] nums) {
        int n =nums.length;
        memo=new int[n];
        if(n<3){
            return Math.max(nums[0],nums[1]);

        }
        memo[0]=nums[0];
        memo[1]=nums[1];
        for (int i =2;i<n;i++){
            memo[i]=Math.max(nums[i]+memo[i-2],memo[i-1]);
        }
        return Math.max(memo[n-1],memo[n-2]);

        
    
        

    }
}
