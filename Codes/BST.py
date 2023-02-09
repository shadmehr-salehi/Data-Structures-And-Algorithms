# ---- A Drunk Man Will Find His Way Home but a Drunk Bird May Get Lost Forever =) ----
# impleting Binary search tree clas in python (AKA BST).

class TreeNode :
    def __init__(self , value):
        self.right = None 
        self.left = None 
        self.value = value 
    
    def insert(self , value):
        if value < self.value:
            if self.left is None:
                self.left =  TreeNode(value)
            else : 
                self.left.insert(value)
        else : 
            if self.right is None:
                self.right = TreeNode(value)
            else :
                self.right.insert(value)
    
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.value)
        if self.right is not None:
            self.right.inorder()
    
    def preorder(self):
        print(self.value)
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.value)

    def find(self ,value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)

        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True

    def min(self):
        while self.left is not None:
            self = self.left
        print (self.value)
    
    def max(self):
        while self.right is not None:
            self = self.right
        print (self.value)


# example
if __name__ == '__main__':

    tree = TreeNode(5)
    tree.insert(10)
    tree.insert(12)
    tree.insert(100)
    tree.insert(2)
    tree.insert(10)
    tree.insert(3)
    print("inorder tree traversal... : ")
    tree.inorder()
    print("preorder tree traversal... : ")
    tree.preorder()
    print("postorder tree traversal... : ")
    tree.postorder()
    print("tree minimum :")
    tree.min()
    print("tree maximum :")
    tree.max()
    #check is 10 is in tree or not 
    print(tree.find(10))


