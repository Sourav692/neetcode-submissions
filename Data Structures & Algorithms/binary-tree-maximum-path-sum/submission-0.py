# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = [float("-inf")]                 # global best answer found anywhere
        def gain(n):                           # returns the best single downward arm from n
            if not n:
                return 0
            left = max(0, gain(n.left))        # ignore a branch that would hurt the sum (clamp to 0)
            right = max(0, gain(n.right))
            best[0] = max(best[0], n.val + left + right)  # a path bending through n uses BOTH arms
            return n.val + max(left, right)    # but we can only hand our PARENT one arm
        gain(root)
        return best[0]