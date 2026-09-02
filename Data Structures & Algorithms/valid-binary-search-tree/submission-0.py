# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, low, high):            # node's value must stay strictly inside (low, high)
            if not node:
                return True                    # empty subtree is fine
            if not (low < node.val < high):    # out of its allowed range -> not a BST
                return False
            # Going left tightens the upper bound; going right tightens the lower bound.
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)
        return valid(root, float("-inf"), float("inf"))
        