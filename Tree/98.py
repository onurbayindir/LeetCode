# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # If the tree is binary search tree
        # The inorder traversal should be sorted
        def getInorder(root):
            if root == None:
                return []
            return getInorder(root.left) + [root.val] + getInorder(root.right)
        inorder = getInorder(root)
        # Iterate from left to right if you see any element is less than
        # current max then inorder is not sorted
        if not inorder:
            return True
        curMax = inorder[0]
        for i in range(1,len(inorder)):
            if inorder[i] <= curMax:
                return False
            curMax = max(curMax, inorder[i])
        # Do the same thing from right to left but this time check the minimum
        curMin = inorder[-1]
        for i in range(len(inorder)-2,-1,-1):
            if inorder[i] >= curMin:
                return False
            curMin = min(curMin, inorder[i])
        return True
        
        