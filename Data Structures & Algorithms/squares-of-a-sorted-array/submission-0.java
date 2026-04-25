class Solution {
    public int[] sortedSquares(int[] nums) {
        int n=nums.length ;
        int[] res= new int[n];
        int l=0;
        int r=nums.length-1 ;
        int k=n-1; 
        while(l<=r){
            if (Math.abs(nums[l])>Math.abs(nums[r])){
                res[k]=nums[l]*nums[l];
                l++;
                k--;
            }
            else {
                res[k]=nums[r]*nums[r];
                r--;
                k--;

            }

        
        }
        return res ; 


        
    }
}