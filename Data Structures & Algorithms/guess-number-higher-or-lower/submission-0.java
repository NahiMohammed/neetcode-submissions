public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int l = 1;
        int r = n;

        while (l <= r) {
            int m = l + (r - l) / 2;

            int res = guess(m);

            if (res == 0) {
                return m;
            } else if (res == -1) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        return -1;
    }
}