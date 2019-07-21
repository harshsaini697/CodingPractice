import heapq
class tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Solution(object):

    min=float('inf')
    nextBig=float('inf')
    arr=[0]*2
    def inorder(root):
        if root:
            Solution.inorder(root.left)

            if root.data<Solution.nextBig:
                if root.data<Solution.min:
                    Solution.nextBig=Solution.min
                    Solution.min=root.data
                else:
                    Solution.nextBig=root.data



            Solution.inorder(root.right)

        Solution.arr[0]=Solution.min
        Solution.arr[1]=Solution.nextBig
        return Solution.arr




if __name__ == '__main__':
    root=tree(2)
    root.left=tree(3)
    root.right=tree(4)
    root.left.left=tree(5)
    root.left.right=tree(1)
    min=float('inf')
    print(Solution.inorder(root))





