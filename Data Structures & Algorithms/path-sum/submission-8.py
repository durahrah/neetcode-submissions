# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathie(node,curSum):
            if not node:
                return False
            curSum+=node.val
            if not node.left and not node.right:
                return curSum==targetSum
            if pathie(node.left,curSum):
                return True
            if pathie(node.right,curSum):
                return True
            return False
        return pathie(root,0) 