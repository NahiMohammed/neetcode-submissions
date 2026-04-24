class Solution {
    public boolean validWordAbbreviation(String word, String abbr) {
        int i = 0; // pointer word
        int j = 0; // pointer abbr

        while (j < abbr.length()) {

            // case 1: letter
            if (Character.isLetter(abbr.charAt(j))) {
                if (i >= word.length() || word.charAt(i) != abbr.charAt(j)) {
                    return false;
                }
                i++;
                j++;
            }

            // case 2: number
            else {
                if (abbr.charAt(j) == '0') return false; // leading zero invalid

                int start = j;

                while (j < abbr.length() && Character.isDigit(abbr.charAt(j))) {
                    j++;
                }

                int num = Integer.parseInt(abbr.substring(start, j));
                i += num;
            }
        }

        return i == word.length();
    }
}