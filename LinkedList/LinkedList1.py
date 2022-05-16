# Creating a node in Python
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=Node(1)
print(node1,'\nData=', node1.data,'Address=', node1.next)