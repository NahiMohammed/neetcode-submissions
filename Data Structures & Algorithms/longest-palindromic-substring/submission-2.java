class Solution {
    public String longestPalindrome(String s) {
        if (s.length()<2){
            return s;
        }
        int res = 0 ; 
        String s_res ="";
        for (int i= 0 ; i<s.length()-1;i++){
            int a = extand(s,i,i);
            if (s.charAt(i)==s.charAt(i+1)){
                int b = extand(s,i,i+1);
                a= Math.max(a,b);

            }
            if (a > res) {
                res = a;

                int start = i - (a - 1) / 2;

                s_res = s.substring(start, start + a);
            }

            
            
        }
        return s_res ; 

        
    }
    private int extand(String s  ,int l , int r){
        while(l>=0 && r <s.length() && s.charAt(l)==s.charAt(r)){
            l--;
            r++;
        }
        return r-l-1 ;

    }
}
