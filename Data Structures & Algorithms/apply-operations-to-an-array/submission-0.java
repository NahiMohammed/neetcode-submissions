class Solution {
    public int[] applyOperations(int[] nums) {

        for(int i =0;i<nums.length-1;i++){
            if (nums[i]==nums[i+1]){
                nums[i]=nums[i]*2;
                nums[i+1]=0;

            }
        }
        int j=0;
        for (int i=0;i<nums.length;i++){
            if (nums[i]!=0){
                int tmp = nums[i];
                nums[j] = nums[i];
                j++;
            }

        }
        for (int k =j ;k<nums.length ;k++){
            nums[k]=0;
        }
        return nums ;
    }
}