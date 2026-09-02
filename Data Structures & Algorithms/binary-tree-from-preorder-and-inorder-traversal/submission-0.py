# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {v: i for i, v in enumerate(inorder)}   # value -> its position in inorder (O(1))
        self_pre = [0]                         # our current position in preorder (in a list so it persists)
        def helper(lo, hi):                    # build the subtree covering inorder[lo..hi]
            if lo > hi:
                return None
            val = preorder[self_pre[0]]        # next preorder value is this subtree's root
            self_pre[0] += 1                   # advance the preorder pointer
            node = TreeNode(val)
            m = idx[val]                       # where the root splits inorder (instant lookup)
            node.left = helper(lo, m - 1)      # build the left part first (preorder does left first)
            node.right = helper(m + 1, hi)     # then the right part
            return node
        return helper(0, len(inorder) - 1)