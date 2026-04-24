class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length; 
        int[] tab = new int[2 * n];
        for (int i =0 ; i<nums.length;i++){
            tab[i]=tab[i+n]=nums[i];
        }
        return tab ;
    }
}