# Creating a node in Python
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL: # SLL -> singly linked list
    def __init__(self):
        self.head=None
    # travarsal of the Linked List
    def travarsal(self):
        if self.head is None:
            print("The Linked List is empty! ")
        else:
            a=self.head
            print("The Linked List is: ",end='')
            while a is not None:
                print(a.data,end=" ")
                a=a.next
            print('\n')

    # size of the Linked list
    def getLength(self):
        LLsize=0
        a=self.head
        while a is not None:
            a=a.next
            LLsize+=1
        return LLsize
        
    # insert a node at the beginning
    def insertAtBegin(self, data):
        new=Node(data)
        new.next=self.head
        self.head=new

    # insert a node at the beginning
    def insertAtEnd(self, data):
        new=Node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=new

    # insert at any position
    def insertAnywhere(self, pos, data):
        size=self.getLength()
        if pos<=0 or pos>size+1:
            print("Can't insert Node! The Location is invalid.")
        elif pos==1:
            self.insertAtBegin(data)
        else:
            new=Node(data)
            a=self.head
            while pos is not 1:
                prev=a
                a=a.next
                pos-=1
            prev.next=new
            new.next=a
        
    # reversing of the Linked List
    def reverseList(self):
        if self.head is None:
            print("The Linked List is empty! ") 
        prev=None
        curr=self.head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        self.head=prev
        
if __name__=="__main__":
    sll=SLL()
    n1=Node(10)
    sll.head=n1
    n2=Node(20)
    n1.next=n2
    n3=Node(30)
    n2.next=n3
    n4=Node(40)
    n3.next=n4
    n5=Node(50)
    n4.next=n5
    sll.travarsal()

    print("Node inserted at the beginning")
    sll.insertAtBegin(5)
    sll.travarsal()

    print("Node inserted at the end")
    sll.insertAtEnd(60)
    sll.travarsal()

    print("Current size of the Linkedlist=",sll.getLength())

    sll.insertAnywhere(4, 25)
    sll.travarsal()