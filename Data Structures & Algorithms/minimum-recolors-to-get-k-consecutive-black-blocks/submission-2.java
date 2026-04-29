class Solution {
    public int minimumRecolors(String blocks, int k) {

        int white = 0;

        // première fenêtre
        for (int i = 0; i < k; i++) {
            if (blocks.charAt(i) == 'W') white++;
        }

        int minWhite = white;

        // sliding window
        for (int i = k; i < blocks.length(); i++) {

            if (blocks.charAt(i) == 'W') white++;
            if (blocks.charAt(i - k) == 'W') white--;

            minWhite = Math.min(minWhite, white);
        }

        return minWhite;
    }
}