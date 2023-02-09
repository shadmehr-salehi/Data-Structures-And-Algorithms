#remove elements from link list whose sum equals to zero 
# ---- A Drunk Man Will Find His Way Home but a Drunk Bird May Get Lost Forever =) ----

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class linkedlist:
    def __init__(self , Head = None):
        self.head = Head
        

    def fix(self,index):
        if index == 1 :
            index = self.head

        if index.next == None :
            return
        temp = index.next.data
        if temp + index.data != 0 :
            self.fix(index.next)
            return

        if index == self.head :
            self.head = index.next.next
            self.fix(self.head)
            return
        
        index.prev.next = index.next.next
        self.fix(index.prev)
        return


    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node

    
    def print(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end =' ')
            current_node = current_node.next
        # print('None')



llist = linkedlist()

n = int(input())
temp = input()
temp = temp.split(" ")
for i in range(n):
    llist.insert(int(temp[i]))




llist.fix(1)
llist.print()


