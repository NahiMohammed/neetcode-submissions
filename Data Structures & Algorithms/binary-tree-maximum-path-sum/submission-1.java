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
    int max=Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        if (root==null){
            return 0 ; 
        }
        if (root.left==null && root.right ==null){
            return root.val;
        }
        if (root.left==null || root.right ==null){
            if (root.left==null){
                return Math.max(maxPathSum(root.right),Math.max(root.val,root.val+maxPathSum(root.right)));
            }
            return Math.max(maxPathSum(root.left),Math.max(root.val,root.val+maxPathSum(root.left)));
            
        }

        int l = maxPathSum(root.left);
        int r = maxPathSum(root.right);


        return Math.max(l+r+root.val,Math.max(l,r));


        
        
    }
}
