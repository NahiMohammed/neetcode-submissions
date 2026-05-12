class Solution {
    public int climbStairs(int n) {

        return dp(n) ;

        
        
    }

    private int dp(int n ){
        if(n<=0){
            return 0;
        }
        else if (n==1){
            return 1;
        }
        else if (n==2){
            return 2;
        }
        return dp(n-2)+dp(n-1);
    }
}
