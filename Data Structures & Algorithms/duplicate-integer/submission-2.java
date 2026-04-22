class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> num_set = new HashSet<Integer>();
        for (int num:nums) {
            if (num_set.contains(num)) {
                return true;  
            }
            num_set.add(num);
        }
        return false;
        
    }
}