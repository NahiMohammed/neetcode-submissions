class Solution {
    private List<List<Integer>> res ;
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        res=new ArrayList<>();
        Arrays.sort(candidates);
        helper(candidates,target,0,0, new ArrayList<Integer>());

        return res;

        
    }
    private void helper(int[] candidates, int target, int total,int start,List<Integer> curr) {
        if(total==target){
            res.add(new ArrayList<>(curr));
            return ;
        }
        
        for (int i =start ;i<candidates.length;i++){
            if (candidates[i]+total>target){
                return ;
            }
            
            if (i > start && candidates[i] == candidates[i - 1]) {
                continue;
            }
            
            curr.add(candidates[i]);
            helper(candidates,target,total+candidates[i],i+1,curr);
            curr.remove(curr.size()-1);
        }


    }
}
