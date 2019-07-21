class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isBalanced(root: TreeNode) -> bool:
    if not root:
        return True
    if depth(root) == -1:
        return False
    else:
        return True


def depth(root):
    if not root:
        return 0
    left = depth(root.left)
    right = depth(root.right)
    if abs(left - right) > 1 or left == -1 or right == -1:
        return -1
    return max(left, right) + 1
#[3,9,20,null,null,15,7]
root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.left=TreeNode(None)
root.right=TreeNode(None)
root.right.right=TreeNode(7)
root.right.left=TreeNode(15)

print(isBalanced(root))