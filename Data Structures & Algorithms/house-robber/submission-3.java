class Solution {
    int[] memo ;
    int m;
    public int rob(int[] nums) {
        int n =nums.length;
        memo=new int[n];
        if(n==1){
            return nums[0];

        }

        if(n<3){
            return Math.max(nums[0],nums[1]);

        }
        memo[0]=nums[0];
        memo[1]=nums[1];
        m=memo[0];
        for (int i =2;i<n;i++){
            memo[i]=nums[i]+m;
            m=Math.max(m,memo[i-1]);
        }
        return Math.max(memo[n-1],memo[n-2]);

        

    }
}
/**
[1,1,4,]
*/
/**
[5,1,7,15,13,17,22]
*/
