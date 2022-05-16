class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inOrderTrv(root):
    if root:
        inOrderTrv(root.left)
        print(root.data,end=" ")
        inOrderTrv(root.right)


if __name__=="__main__": 
    root=a=Node('a')
    b=Node('b')
    c=Node('c')
    a.left=b
    a.right=c
    inOrderTrv(root)
    # print(a.data,a.left.data,a.right.data)

