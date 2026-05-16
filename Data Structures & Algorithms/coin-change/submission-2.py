class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0]=0
        for i in range(1,amount+1):
        
            for c in coins : 
                if i>=c:
                    dp[i]=min(dp[i],1+dp[i-c])
        return dp[amount] if dp[amount] != amount + 1 else -1



"""
class Solution {

    public List<List<Integer>> combinationSum(int[] nums, int target) {
        res= new ArrayList<>();
        Arrays.sort(nums);
        
        
        return res;


        
    }
    private void dfs(int debut , List<Integer>curr , Integer total , int[] nums ,int  target){
        if (total==target){
            res.add(new ArrayList<>(curr));
            return ;
        }
        
        for (int i =debut ; i<nums.length;i++){
            if (total+nums[i]>target){
                return;
            }
            
            curr.add(nums[i]);
            dfs(i , curr , total+nums[i] ,nums ,target);
            curr.remove(curr.size()-1);

        }
    }
}"""