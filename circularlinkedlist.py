class Node:
    
    def __init__(self,value, next = None):
        self.value = value;
        self.next =next;
        
class LinkedList:
    
    def __init__(self):
        self.head =None;
        
    def append(self,value): #adding the member at the last
        if self.head == None:
            self.head = Node(value);
            self.head.next = self.head;
            
        else:
            t = self.head
            while(t.next != self.head):
                t= t.next;
            
            t.next =Node(value);
            t.next.next =self.head;
            
    def remove(self,value): #removing the Node by value
        if self.head ==None:
            print('There are no values in linkedlist to remove.');
            
        else:
            t =self.head;
            if t.value == value:
                while(t.next != self.head):
                    t= t.next;
                
                self.head =self.head.next;
                t.next = self.head;
                
            else:
                while t.next :
                    if t.next.value ==value:
                        a =t.next.next;
                        t.next =a;
                        break;
                    else:
                        t =t.next;
                print('There is no such value in this linkedlist');
            
                
                    
                    
                
        
            
    def printall(self):
        t = self.head
        while t.next!=self.head:
            print(t.value);
            t =t.next;
        print(t.value);
                
        
llist = LinkedList()
llist.append(20)
llist.append(4)
llist.append(15)
llist.append(10)
 
# Create a loop for testing
llist.head.next.next.next.next == llist.head 