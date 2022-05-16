class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    def show(self):
        print(self.data)

class LinkedList:
    def __init__(self) :
        self.head=None
    def insert_at_begin(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_at_end(self,data):
        temp=self.head
        node=Node(data,self.head)
        node.next=None
        if temp is None:
            self.head=node
        else:
            while temp.next:
                temp=temp.next
            temp.next=node

    def insert_at_pos(self,pos,data):
        if(pos==1):
            self.insert_at_begin(self,data)
            return
        else:
            temp=self.head
            while pos!=1:
                prev=temp
                temp=temp.next
                pos-=1 
            a=Node(data,None)
            a.next=prev.next
            prev.next=a
        return

    def Delete_at_pos(self,pos):
        temp=self.head
        if(pos==1):
            print(self.head.data,' deleted')  
            self.head=self.head.next
            return
        if(pos<1):
            print('Please Enter a valid location!!')
            return
        while pos!=1:
            prev=temp
            temp=temp.next
            pos-=1 
        print(prev.next.data,' deleted')       
        prev.next=temp.next

    def PrintLL(self):
        if self.head is None:
            print("List is empty!!")
            return 
        else:
            n=self.head
            My_string=''
            while n:
                print(n.data,end=" ")
                My_string+=str(n.data)+'-->'
                n=n.next
        # print(My_string)

LL1=LinkedList()
LL1.insert_at_begin(5)
LL1.insert_at_begin(2)
LL1.insert_at_begin(8)
LL1.insert_at_begin(9)
LL1.insert_at_end(4)
LL1.insert_at_end(1)
LL1.insert_at_begin(10)
LL1.PrintLL()
print('')
# LL1.Delete_at_pos(1)
LL1.insert_at_pos(6,12)
LL1.PrintLL()

