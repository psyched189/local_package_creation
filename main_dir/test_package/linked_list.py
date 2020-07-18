class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def print_nodes(self):
        curr = self
        while curr:
            print(curr.val)
            curr = curr.next
           
            
class LinkedList:
    def __init__(self):
        self.head = None
       
    def append(self, val):
        new_node = Node(val)
        
        if not self.head:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = new_node
        
    
           
