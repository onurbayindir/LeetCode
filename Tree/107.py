# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # create a list of lists for storing the nodes for each level
        # Do top-down traversal 
        if root == None:
            return None
        queue = [root]
        level = [[root]]
        while queue:
            newLevel = []
            for node in queue:
                if node.left != None:
                    newLevel.append(node.left)
                if node.right != None:
                    newLevel.append(node.right)
            if newLevel:
                level.append(newLevel)
            queue = newLevel
        for l in level:
            for i in range(len(l)):
                l[i] = l[i].val
        return level[::-1]