# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        out = []
        def dfs(n):                            # preorder walk, writing '#' for empty children
            if not n:
                out.append("#")               # marker records where a child is missing
                return
            out.append(str(n.val))            # record this node's value
            dfs(n.left); dfs(n.right)         # then its left subtree, then its right
        dfs(root)
        return ",".join(out)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = iter(data.split(","))          # read tokens in the SAME order serialize wrote them
        def build():
            v = next(vals)
            if v == "#":                      # a '#' means "no node here"
                return None
            node = TreeNode(int(v))
            node.left = build()               # rebuild left subtree first (matches preorder)
            node.right = build()              # then the right subtree
            return node
        return build()
