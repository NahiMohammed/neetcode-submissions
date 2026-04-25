class Solution {
    public int findContentChildren(int[] g, int[] s) {
        int i = 0;
        int j = 0;
        int res = 0;
        Arrays.sort(g);
        while (j<s.length && i<g.length){
            if (s[j]>=g[i]){
                j++;
                i++;
                res++;
            }
            else{
                j++;
            }
        }
        return res ; 

    }
}