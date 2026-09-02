# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        while node:
            if p.val < node.val and q.val < node.val:  # both targets are smaller -> go left
                node = node.left
            elif p.val > node.val and q.val > node.val:# both targets are larger -> go right
                node = node.right
            else:                              # they split here (one each side, or equal)
                return node             # this is the lowest common ancestor
        return -1