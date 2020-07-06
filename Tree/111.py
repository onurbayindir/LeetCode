# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        tree = [[root]]
        height = 1
        queue = [root]
        while queue:
            newQueue = []
            for node in queue:
                if node.left == None and node.right == None:
                    return height
                if node.left != None:
                    newQueue.append(node.left)
                if node.right != None:
                    newQueue.append(node.right)
            queue = newQueue
            height += 1
        return height