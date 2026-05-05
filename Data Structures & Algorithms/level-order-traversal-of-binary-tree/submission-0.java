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
    public List<List<Integer>> levelOrder(TreeNode root) {
        HashMap<Integer,List<Integer>> map = new HashMap<>();
        List<List<Integer>> res= new ArrayList<>();
        if (root==null){
            return res;
        }
        Stack<Pair<TreeNode, Integer>> stack = new Stack<>();
        stack.push(new Pair<>(root, 1));
        while (!stack.isEmpty()){
            Pair<TreeNode, Integer> current = stack.pop();
            TreeNode node = current.getKey();
            int depth =current.getValue();
            map.putIfAbsent(depth, new ArrayList<>());
            map.get(depth).add(node.val);
            if (node.right!=null){
                stack.push(new Pair<>(node.right, depth + 1));
            }
            if (node.left!=null){
                stack.push(new Pair<>(node.left, depth + 1));
            }

        }
        List<List<Integer>> result = new ArrayList<>(map.values());
        return result; 


        
    }
}
