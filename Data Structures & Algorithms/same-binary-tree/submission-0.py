# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True                        # both empty here -> matching so far
        if not p or not q or p.val != q.val:
            return False                       # one empty, or values differ -> not the same
        # Values match; now the left subtrees must match AND the right subtrees must match.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)