#Full linked List implementation 
# ---- A Drunk Man Will Find His Way Home but a Drunk Bird May Get Lost Forever =) ----
# Linked List in python

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Linked List class
class LinkedList:
    def __init__(self , Head = None):
        self.head = Head
        
    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
    
    def insert_at_head(self,data):
        if self.head is None:
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            new_node.next.prev = new_node

            
    def print(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end ='->')
            current_node = current_node.next
        print('None')

    def size(self):
        current_node = self.head
        count = 0 
        while current_node is not None:
            count += 1 
            current_node = current_node.next
        return count
    
    def delete_by_value(self,value):
        current_node = self.head
        previous_node : Node()
        while True:
            if current_node.data == value:
                previous_node.next = current_node.next 
                break
            else:
                previous_node = current_node
                current_node = current_node.next

    def delete_by_index(self,index):
        current_node = self.head 
        previous_node :Node()
        Current_index = 0 
        while Current_index is not index:
            previous_node = current_node
            current_node = current_node.next
            Current_index += 1 
        
        previous_node.next = current_node.next

    def exists(self,value):
        current_node = self.head 
        while current_node is not None:
            if current_node.data is value:
                return True
            else:
                current_node = current_node.next
            return False

    def reverse(self):
        current_node = self.head 
        while current_node is not None:
            self.head = current_node
            next_node = current_node.next
            current_node.next = current_node.prev
            current_node.prev = current_node.next
            current_node = next_node



 


if __name__ == '__main__':
    # Inserting data in Linked List
    llist = LinkedList()
    llist.insert_at_tail(1)
    llist.insert_at_tail(2)
    llist.insert_at_tail(3)
    llist.insert_at_tail(4)
    llist.insert_at_tail(5)
    llist.reverse()
    llist.print()

    # print(llist.head)
    
    # llist.delete_by_index(1)
    # llist.print()
    # print(llist.exists(10))
    # print(llist.size())
          
        
