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

    def is_empty(self):
        if self.root:
            return True
        return False

    def inorder(self):
        def _inorder_travasal(root):
            if root is None:
                return
            _inorder_travasal(root.left)
            print("->", root.data, end=" ")
            _inorder_travasal(root.right)

        _inorder_travasal(self.root)

    def postorder(self):
        def _postorder_travasal(root):
            if root is None:
                return
            _postorder_travasal(root.left)
            _postorder_travasal(root.right)
            print("->", root.data, end=" ")

        _postorder_travasal(self.root)
    def traverse(self):
        if self.root is None:
            return print("This is an empty binary search tree.")
        print("Preorder: ",end = "")
        self.preorder()
        print()
        print("Inorder: ",end = "")
        self.inorder()
        print()
        print("Postorder: ",end = "")
        self.postorder()
        print()

    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data
    
    def delete(self,data : int):
        def _delete_node(root, data):
            if root is None:
                return root, None 
            
            if data < root.data:
                root.left, deleted_node = _delete_node(root.left, data)
            elif data > root.data:
                root.right, deleted_node = _delete_node(root.right, data)
            else:
                deleted_node = root
                if root.left is None and root.right is None:
                    return None, deleted_node
                elif root.left is None:
                    return root.right, deleted_node
                elif root.right is None:
                    return root.left, deleted_node
                else:
                    max_left = self._find_max_left(root.left)
                    root.data = max_left
                    root.left, _ = _delete_node(root.left, max_left)
            
            return root, deleted_node

        self.root, deleted_node = _delete_node(self.root, data)
        
        if deleted_node is None:
            print("Delete Error, "+str(data)+" is not found in Binary Search Tree.")
            return None
        else:
            return deleted_node.data

    def _find_max_left(self, root: BSTNode):
        while root.right is not None:
            root = root.right
        return root.data

def main():
  my_bst = BST()
  while 1:
    text = input()
    if text == "Done":
      break
    condition, data = text.split(": ")
    if condition == "I":
      my_bst.insert(int(data))
    elif condition == "D":
      my_bst.delete(int(data))
    else:
      print("Invalid Condition")
  my_bst.traverse()

main()