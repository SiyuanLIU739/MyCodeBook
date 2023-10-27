import javax.swing.tree.TreeNode;

public class Q98 {
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

    public boolean isValidBST(TreeNode root) {
        boolean check;
        int extreme;

        if(root.left != null){
            check = isValidBST(root.left);
            if(check == false){
                return false;
            }

            if(root.left.val >= root.val){
                return false;
            }

            extreme = this.maxInSubtree(root.left);
            if(extreme >= root.val){
                return false;
            }
        }

        if(root.right != null){
            check = isValidBST(root.right);
            if(check == false){
                return false;
            }

            if(root.right.val <= root.val){
                return false;
            }

            extreme = this.minInSubtree(root.right);
            if(extreme <= root.val){
                return false;
            }
        }

        return true;
    }

    public int minInSubtree(TreeNode root){
        if(root.left == null){
            return root.val;
        }
        return minInSubtree(root.left);
    }

    public int maxInSubtree(TreeNode root){
        if(root.right == null){
            return root.val;
        }
        return maxInSubtree(root.right);
    }

}
