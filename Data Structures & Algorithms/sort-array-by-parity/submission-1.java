class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int l=0;
        int n=nums.length;
        int r=n-1;
        while(l<r){
            if ((nums[l]&1)==1){
                int tmp=nums[r];
                nums[r]=nums[l];
                r--;
                nums[l]=tmp;
            }else{
                l++;
            }
        }
        return nums ;
        
    }
}