class Solution {
    public int characterReplacement(String s, int k) {
        int l = 0 ; 
        Set<Character> set  =new HashSet<>();
        int a = 0;
        int res=0 ;
        for (int r=0 ; r<s.length(); r++){
            if(s.charAt(l)==s.charAt(r)){
                continue ;
                

            }
            else {
                if (!(a==k)){
                    a++;

                }
                else {
                    res=Math.max(res,r-l);
                    l=r-k+1;
                    a=0;

                }
            }
        }
        return Math.max(s.length()-l,res);
    }
}
