class Solution {
    private int start ;
    private int color ;
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        this.color= color ;         
        start = image[sr][sc];
        image[sr][sc]=color ;
        if(start==color){
            return image;
        }
        flood(image,sr,sc);
        return image ;


        
    }
    private void flood(int[][] image, int sr, int sc){

    if (sc - 1 >= 0 && image[sr][sc-1]==start) {
        image[sr][sc-1]=color;
        flood(image, sr, sc - 1);
    }

    // right
    if (sc + 1 < image[0].length && image[sr][sc+1]==start) {
        image[sr][sc+1]=color;
        flood(image, sr, sc + 1);
    }

    // up
    if (sr - 1 >= 0 && image[sr-1][sc]==start) {
        image[sr-1][sc]=color;
        flood(image, sr - 1, sc) ;
    }

    // down
    if (sr + 1 < image.length && image[sr+1][sc]==start) {
        image[sr+1][sc]=color;
        flood(image, sr + 1, sc);
    }

    }
}