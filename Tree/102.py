# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        levelOrderTraversal = [[root]]
        curLevel = [root]
        while curLevel:
            newLevel = []
            for node in curLevel:
                if node.left != None:
                    newLevel.append(node.left)
                if node.right != None:
                    newLevel.append(node.right)
            if newLevel:
                levelOrderTraversal.append(newLevel)
            curLevel = newLevel
        for level in levelOrderTraversal:
            for i in range(len(level)):
                level[i] = level[i].val
        return levelOrderTraversal