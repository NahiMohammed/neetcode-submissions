class Solution {
    public String minWindow(String s, String t) {
        if (s.length()<t.length()){
            return "";
        }
        HashSet<Character> set = new HashSet<>();
        for (int i =0; i<t.length();i++){
            set.add(t.charAt(i));
        }
        int r = 0;
        int l = -1;
        int res = Integer.MAX_VALUE;
        int resl = 0;
        HashSet<Character> set1 = new HashSet<>(set);
        while (r<s.length()){
            System.out.println(set1);
            if (set1.contains(s.charAt(r))){
                if(l==-1){
                    l=r;
                }
                set1.remove(s.charAt(r));
                
                
                

            }
            if (set1.size()==0){
                if ((r-l+1)<res){
                    System.out.println(r-l);
                    resl=l;
                    res=r-l+1;
                    l=-1;
                }
                set1=new HashSet<>(set);

            }
            r++;
            


        }
        System.out.println(resl);
        return s.substring(resl,resl+res) ;


        
    }
}
