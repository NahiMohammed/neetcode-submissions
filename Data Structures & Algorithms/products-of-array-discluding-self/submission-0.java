class Solution {
    public int[] productExceptSelf(int[] nums) {
        int  n= nums.length; 
        int[] prefix = new int[n];
        int[] suffix = new int[n];
        int[] res = new int[n];
        for(int i=0 ; i<n ; i++) {
            prefix[i]=1;
            suffix[i]=1;
        }
        for (int i=1 ; i<n;i++){
            prefix[i]=prefix[i-1]*nums[i-1];
        }
        for (int i=n-2 ; i>-1;i--){
            suffix[i]=suffix[i+1]*nums[i+1];
        }
        for (int i=0 ; i<n;i++){
            res[i]=suffix[i]*prefix[i];
        }
        return res;


    
        
    }
}  
//prefix = [1,1,2,8] 
//suffix = [48,24,6,1]