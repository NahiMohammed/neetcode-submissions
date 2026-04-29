class Solution {
    public int minimumDifference(int[] nums, int k) {
        Arrays.sort(nums);
        int  l =0 ;
        int res=Integer.MAX_VALUE ;
        System.out.println(Arrays.toString(nums));
        for(int r=k-1;r<nums.length ;r++ ){
            System.out.println(nums[r]);
            System.out.println(nums[r-k+1]);
            res=Math.min(nums[r]-nums[r-k+1],res);

        }
        return res;
        
    }
}