class node:
    def _init_(self,data=None):
        self.data=data 
        self.next=None

class linkedlist:
    def _init_(self):
        self.head=node()

    def accept_data(self,data):
        new_node = node(data)
        cur=self.head
        while cur.next !=None:
            
            cur=cur.next
        cur.next=new_node

    
    def display(self):
        disp=[]
        cur=self.head

       
        while cur.next !=None:
            cur=cur.next
            disp.append(cur.data)

            print(disp)



l=linkedlist()
l.accept_data(2)
l.accept_data(3)
l.accept_data(4)
l.accept_data(6)

l.display()

        

