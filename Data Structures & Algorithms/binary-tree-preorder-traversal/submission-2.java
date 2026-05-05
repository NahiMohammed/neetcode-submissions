/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        Stack<TreeNode> st = new Stack<TreeNode>();
        TreeNode cur = root;
        List<Integer> res = new ArrayList<>();

        while (cur != null || !st.isEmpty()) {
            if (cur != null) {
                res.add(cur.val);
                st.push(cur.right);
                cur = cur.left;
            } else {
                cur = st.pop();
            }
        }

        return res;
    }
}
