class Solution {
    private int[] memo ;
    public int minCostClimbingStairs(int[] cost) {
        if (cost.length<=2){
            return Math.min(cost[0],cost[1]);
        }
        memo = new int[cost.length];
        memo[0]=cost[0];
        memo[1]=cost[1];
        for (int i = 2;i<cost.length;i++){
            memo[i]=cost[i]+Math.min(memo[i-1],memo[i-2]);
            System.out.println(memo[i]);
        }
        
        return Math.min(memo[cost.length-1],memo[cost.length-2]);
        
    }

}
/**
memo=[1,2,]
*/

