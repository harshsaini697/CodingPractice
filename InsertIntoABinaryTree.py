class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(temp):
    if not temp:
        return
    inorder(temp.left)
    print(temp.data,end=" ")
    inorder(temp.right)

def insert(temp,key):
    q=[]
    q.append(temp)
    while(len(q)):
        temp=q.pop(0)
        if not temp.left:
            temp.left=Node(key)
            break
        else:
            q.append(temp.left)
        if not temp.right:
            temp.right=Node(key)
            break
        else:
            q.append(temp.right)



    return

if __name__ == '__main__':
    root=Node(10)
    root.left=Node(11)
    root.left.left=Node(7)
    root.right=Node(9)
    root.right.left = Node(15)
    root.right.right=Node(8)
    #inorder(root)

    insert(root,12)

    inorder(root)