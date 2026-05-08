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

public class Codec {
    private List<Integer> ino;
    private List<Integer> pre;

    private List<Integer> inorderTraversal(TreeNode root) {
        ino = new ArrayList<>();
        inorder(root);
        return ino;
    }

    private void inorder(TreeNode node) {
        if (node == null) {
            return;
        }
        inorder(node.left);
        ino.add(node.val);
        inorder(node.right);
    }
    
    public List<Integer> preorderTraversal(TreeNode root) {
        pre=new ArrayList<>();
        preoreder(root);
        return pre ;
        
    }
    private void preoreder(TreeNode n){
        if(n==null){
            return ;

        }
        pre.add(n.val);
        preoreder(n.left);
        preoreder(n.right);
    }
    private Map<Integer, Integer> inorderMap;
    private int preorderIndex;

    public TreeNode buildTree(int[] preorder, int[] inorder) {

        inorderMap = new HashMap<>();
        preorderIndex = 0;

        for (int i = 0; i < inorder.length; i++) {
            inorderMap.put(inorder[i], i);
        }

        return build(preorder, 0, inorder.length - 1);
    }

    private TreeNode build(int[] preorder, int left, int right) {
        if (left > right) return null;

        int rootVal = preorder[preorderIndex++];
        TreeNode root = new TreeNode(rootVal);

        int index = inorderMap.get(rootVal);

        root.left = build(preorder, left, index - 1);
        root.right = build(preorder, index + 1, right);

        return root;
    } 



    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        ino = inorderTraversal(root);
        pre = preorderTraversal(root);
        String s1 = ino.toString();
        String s2 = pre.toString();
        return s1+s2 ;
    }


        

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String s1) {
        String[] parts = s1.split("\\]\\[");

        parts[0] = parts[0].replace("[", "");
        parts[1] = parts[1].replace("]", "");

        int[] arr1 = Arrays.stream(parts[0].replaceAll("[\\[\\]]", "").split(","))
                .map(String::trim)
                .filter(s -> !s.isEmpty())
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] arr2 = Arrays.stream(parts[1].replaceAll("[\\[\\]]", "").split(","))
                .map(String::trim)
                .filter(s -> !s.isEmpty())
                .mapToInt(Integer::parseInt)
                .toArray();
        return buildTree(arr2, arr1);
        
                
    }
}


