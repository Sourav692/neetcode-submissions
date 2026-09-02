# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack, node, count = [], root, 0
        while stack or node:
            while node:                        # dive to the smallest unvisited node
                stack.append(node)
                node = node.left
            node = stack.pop()
            count += 1                         # we've now visited one more value (in sorted order)
            if count == k:                     # reached the k-th smallest...
                return node.val                # ...return it immediately (no need to continue)
            node = node.right
        return -1