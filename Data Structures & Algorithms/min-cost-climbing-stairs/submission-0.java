class Solution {
    private int n ;
    private int res;

    public int minCostClimbingStairs(int[] cost) {
        n = cost.length;
        res= 0;
        return Math.min(min(cost,0),min(cost,1));

        
    }
    private int min(int[] cost ,int i ){
        if (i>=n){
            return 0;
        }
        return cost[i]+  Math.min(min(cost,i+1),min(cost,i+2));
    }
}
