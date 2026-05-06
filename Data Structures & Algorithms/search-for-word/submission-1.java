class Solution {
    private int row;
    private int col;
    private Set<Pair<Integer, Integer>> path = new HashSet<>();

    public boolean exist(char[][] board, String word) {
        row = board.length;
        col = board[0].length;

        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                if (backtracking(board, word, r, c, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean backtracking(char[][] board, String word, int r, int c, int indice) {
        if (indice == word.length()) {
            return true;
        }

        if (r >= row || c >= col || r < 0 || c < 0 || board[r][c] != word.charAt(indice)
            || path.contains(new Pair<>(r, c))) {
            return false;
        }
        if (board[r][c] == word.charAt(indice)) {
            path.add(new Pair<>(r, c));
            boolean res = backtracking(board, word, r + 1, c, indice + 1)
                || backtracking(board, word, r - 1, c, indice + 1)
                || backtracking(board, word, r, c + 1, indice + 1)
                || backtracking(board, word, r, c - 1, indice + 1);
            path.remove(new Pair<>(r, c));
            return res;
        }
        return false;
    }
}
