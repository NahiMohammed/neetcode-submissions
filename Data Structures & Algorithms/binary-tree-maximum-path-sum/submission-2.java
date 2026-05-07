class Solution {
    int max = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        dfs(root);
        return max;
    }

    private int dfs(TreeNode node) {
        if (node == null) return 0;

        int left = Math.max(0, dfs(node.left));
        int right = Math.max(0, dfs(node.right));

        // best path THROUGH this node
        max = Math.max(max, node.val + left + right);

        // return best downward path
        return node.val + Math.max(left, right);
    }
}