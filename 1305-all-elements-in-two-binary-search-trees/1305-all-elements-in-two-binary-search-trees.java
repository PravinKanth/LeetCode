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
    public void func(TreeNode root,List<Integer> ar){
        if(root==null){
            return;
        }
        ar.add(root.val);
        func(root.left,ar);
        func(root.right,ar);
    }


    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
     List<Integer>ar=new ArrayList<Integer>();
     func(root1,ar);
     func(root2,ar);
     Collections.sort(ar);
     return ar;
    }

}