class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth( root: TreeNode) -> int:

    if root is None:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
print(maxDepth(root))
