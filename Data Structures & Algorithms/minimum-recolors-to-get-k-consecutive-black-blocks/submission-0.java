class Solution {
    public int minimumRecolors(String blocks, int k) {
        int res=0 ;
        for(char c :blocks.toCharArray()){

        }
        for(int i =0 ;i<k;i++){
            if (blocks.charAt(i)=='W'){
                res++;
            }
            
        }
        int res1=res;
        for( int i =k;i<blocks.length();i++){
            if (blocks.charAt(i)=='W'){
                res1++;
            }
            if (blocks.charAt(i-k)=='W'){
                res1--;
            }
            res=Math.min(res,res1);
            res1=res ;


        }
        return res ;
        
    }
}