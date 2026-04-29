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
        int ress=res;
        for( int i =k;i<blocks.length();i++){
            if (blocks.charAt(i)=='W'){
                res++;
            }
            if (blocks.charAt(i-k)=='W'){
                res--;
            }
            ress=Math.min(res,ress);
            


        }
        return ress ;
        
    }
}