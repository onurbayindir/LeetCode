# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # The order of nodes in inorder is left - root - right
        if root == None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)