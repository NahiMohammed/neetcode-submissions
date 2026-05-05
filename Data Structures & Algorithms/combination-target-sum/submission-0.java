class Solution {
    private List<List<Integer>> res;
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        res= new ArrayList<>();
        Arrays.sort(nums);
        dfs(0 ,new ArrayList<>() ,0  , nums , target);
        
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
}
