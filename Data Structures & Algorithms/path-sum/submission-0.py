# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathie(node,path):
            if not node:
                return False
            path.append(node.val)
            if not node.left and not node.right and sum(path)==targetSum:
                return True
            if pathie(node.left,path):
                return True
            if pathie(node.right,path):
                return True
            path.pop()
            return False
        return pathie(root,[])    


        