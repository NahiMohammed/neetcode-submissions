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
    private List<List<Integer>> res ;
    public List<List<Integer>> levelOrder(TreeNode root) {
        res = new ArrayList<>();
        dfs(root,0);
        return res;     
    }
    private void dfs(TreeNode n,int d){
        if (n==null){
            return ;
        }
        if(res.size()==d){
            res.add(new ArrayList<>());
        }

        res.get(d).add(n.val);
        dfs(n.left, d + 1);
        dfs(n.right, d + 1);


    }
}
