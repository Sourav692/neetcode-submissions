# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def ser(node):                         # flatten a tree to a string, shape included
            if not node:
                return "#"                     # '#' marks an empty child (so shape is captured)
            return "^" + str(node.val) + " " + ser(node.left) + " " + ser(node.right)
        return ser(subRoot) in ser(root)           # sub is a subtree iff its string sits inside root's
        