public class Solution {
    public int mySqrt(int x) {
        int l = 0, r = x;
        int res = 0;

        while (l <= r) {
            long m = l + (r - l) / 2;
            long sq = m * m;

            if (sq > x) {
                r = (int)m - 1;
            } else if (sq < x) {
                l = (int)m + 1;
                res = (int)m;
            } else {
                return (int)m;
            }
        }

        return res;
    }
}