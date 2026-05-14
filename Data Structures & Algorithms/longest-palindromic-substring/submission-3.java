class Solution {

    public String longestPalindrome(String s) {

        if (s.length() < 2) {
            return s;
        }

        int maxLen = 1;
        String res = s.substring(0, 1);

        for (int i = 0; i < s.length(); i++) {

            int odd = expand(s, i, i);
            int even = expand(s, i, i + 1);

            int len = Math.max(odd, even);

            if (len > maxLen) {

                maxLen = len;

                int start = i - (len - 1) / 2;

                res = s.substring(start, start + len);
            }
        }

        return res;
    }

    private int expand(String s, int left, int right) {

        while (
            left >= 0 &&
            right < s.length() &&
            s.charAt(left) == s.charAt(right)
        ) {
            left--;
            right++;
        }

        return right - left - 1;
    }
}