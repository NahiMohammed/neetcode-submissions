class Solution {
    public boolean validPalindrome(String s) {
        if (isP(s)){
            return true ;
        }
        for (int i=0 ; i<s.length(); i++){
            
            if ( isP(s.substring(0,i)+s.substring(i+1)) ){
                
                return true ;
            }
        }
        
        return false; 
    }

    private boolean isP(String s){
        int l=0;
        int r=s.length()-1;
        while(l<r){
            if (s.charAt(l)==s.charAt(r)){
                l++;
                r--;
            }
            else {
                return false;
            } 
        }
        return true ; 
    }


}