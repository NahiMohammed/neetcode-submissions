class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l = 0 ;
        int longest=0 ;
        Set<Character> set = new HashSet<>();
        for (int i=0 ; i<s.length();i++) {
            if (!set.contains(s.charAt(i))){
                set.add(s.charAt(i));
            } else {
                longest = Math.max(longest,set.size());
                while(set.contains(s.charAt(i))){
                    
                    set.remove(s.charAt(l));
                    l++;

                }
                set.add(s.charAt(i));


            }
        }
        return Math.max(longest,set.size());
        
    }
}
