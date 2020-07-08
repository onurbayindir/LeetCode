# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # Do a level by level bread first search
        # check the last element in each level
        if root == None:
            return []
        levels = [[root.val]]
        queue = [root]
        while queue:
            newQueue = []
            newLevel = []
            for node in queue:
                if node.left != None:
                    newQueue.append(node.left)
                    newLevel.append(node.left.val)
                if node.right != None:
                    newQueue.append(node.right)
                    newLevel.append(node.right.val)
            if newQueue:
                levels.append(newLevel)
            queue = newQueue
        rightSideView = []
        for level in levels:
            rightSideView.append(level[-1])
        return rightSideView