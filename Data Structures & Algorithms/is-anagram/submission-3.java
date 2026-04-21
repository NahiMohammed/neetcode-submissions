
class Solution {
    public boolean isAnagram(String s, String t) {
        int n=s.length();
        int m=t.length();
        if (n!=m ) {
            return false;
        }
        int [] arr = new int[26];
        for(int i=0; i<s.length() ;i++ ) {
            arr[s.charAt(i) - 'a']++;
            arr[t.charAt(i) - 'a']--;
        }
        
        for (int x : arr) {
            if (x != 0) return false;
        }
        return true;
    }
}
