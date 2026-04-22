class Solution {
    public int maxArea(int[] heights) {
        int max=0;
        int l=0;
        int r = heights.length -1;
        int volume ;
        int res=0;
        while (l<r) {
            volume = Math.min(heights[l],heights[r])*(r-l);
            res=Math.max(res,volume);
            if (heights[l]>heights[r]){
                r--;

            }      
            else{
                l++;
            }     

        }
        return res;
    }
}
