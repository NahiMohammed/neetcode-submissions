class Solution {
    private ArrayList<List<Integer>> set ;
    public List<List<Integer>> subsets(int[] nums) {
        set =new ArrayList<>();
        List<Integer> subset = new ArrayList<>();
        helper(nums,0,subset);
        return set ;
    }
    private void helper(int[] nums,int index, List<Integer> subset){
        if (index>=nums.length){
            set.add(new ArrayList<>(subset));
            return ; 
        }
        subset.add(nums[index]);
        helper(nums,index+1,subset);
        subset.remove(subset.size()-1);
        helper(nums,index+1,subset);



    }
}
