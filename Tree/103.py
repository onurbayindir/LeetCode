# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # Do level order traversal and then 
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
        for i in range(len(levelOrderTraversal)):
            level = levelOrderTraversal[i]
            for j in range(len(level)):
                level[j] = level[j].val
            if i % 2 == 1:
                levelOrderTraversal[i] = level[::-1]
        return levelOrderTraversal