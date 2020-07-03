# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Do inorder traversal and switch the two elements
        # that are not in the right place
        def getInorder(root):
            if root == None:
                return []
            return getInorder(root.left) + [root.val] + getInorder(root.right)
        inorder = getInorder(root)
        if not inorder:
            return None
        first = None
        second = None
        for i in range(len(inorder)):
            if i > 0 and i < len(inorder) - 1:
                if inorder[i] >= inorder[i-1] and inorder[i] >= inorder[i+1] and not first:
                    first = inorder[i]
                if inorder[i] <= inorder[i-1] and inorder[i] <= inorder[i+1]:
                    second = inorder[i]
            elif i > 0:
                if inorder[i] <= inorder[i-1]:
                    second = inorder[i]
            elif i < len(inorder) - 1:
                if inorder[i] >= inorder[i+1]:
                    first = inorder[i]
        # Do any tree traversal and change the node values
        queue = [root]
        nodeOne = None
        nodeTwo = None
        while queue:
            node = queue.pop()
            if node.val == first:
                nodeOne = node
            elif node.val == second:
                nodeTwo = node
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        nodeOne.val = second
        nodeTwo.val = first
        return root
                        