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
    
    
    public boolean hasPathSum(TreeNode root, int targetSum) {
        return helper(root,targetSum,0);

    }
    private boolean helper(TreeNode root, int targetSum, int sum){
        if (root==null){
            if (targetSum==sum){
                return true ;
            }else {
                return false ;
            }

        }
        return helper(root.left, targetSum,root.val)||helper(root.right, targetSum,root.val);

    }
        
}
/*
        1
       / \
      1   0
     /
    1
*/









