#Classe construtora da árvore binária
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

#Função inserir valor a esquerda

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = BinaryTree
        

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = BinaryTree


    def visit(self):
        print(self.value)


    def pre_order(self):

        print(self.value)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()    
            
        
            



    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print(self.value)
        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.value)


a_node = BinaryTree('a')
print(a_node.value)
a_node.insert_left('b')
b_node = a_node.left_child
print(b_node.value)
a_node.insert_right('c')
c_node = a_node.right_child
print(c_node.value)
b_node.insert_right('d')
d_node = b_node.right_child
print(d_node.value)
c_node.insert_left('e')
e_node = c_node.left_child
print(e_node.value)
c_node.insert_right('f')
f_node = c_node.right_child
print(f_node.value)

print("em pre ordem")
a_node.pre_order()
print("em ordem")
a_node.in_order()
print("pos ordem")
a_node.post_order()