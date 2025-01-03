class BSTNode:
    def __init__(self, data: int=None):
        self.left = None
        self.right = None
        self.data = data
class BST:
    def __init__(self):
        self.root = None
    def insert(self, data: int):
        def _insert_node(root, data):
            if root is None:
                return BSTNode(data)
            if data < root.data:
                root.left = _insert_node(root.left, data)
            else:
                root.right = _insert_node(root.right, data)
            return root
        
        self.root = _insert_node(self.root, data)
    def preorder(self):
        def _preorder_traversal(root):
            if root is None:
                return
            print("->" ,root.data, end=" ")
            _preorder_traversal(root.left)
            _preorder_traversal(root.right)

        _preorder_traversal(self.root)

def main():
  my_bst = BST()
  for i in range(int(input())):
    my_bst.insert(int(input()))
    
  print("Preorder: ", end="")
  my_bst.preorder()

main()