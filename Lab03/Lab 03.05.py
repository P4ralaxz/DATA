class DataNode:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    def insert_last(self, data):
        new_node = DataNode(data)
        self.count += 1
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_front(self, data):
       new_node = DataNode(data)
       self.count += 1
       new_node.next = self.head
       self.head = new_node

    def insert_before(self,node , data):
        self.count += 1
        new_node = DataNode(data)
        if not self.head:
            print("Cannot insert, "+node+" does not exist.")
            return 
        if self.head.data == node:
            new_node = DataNode(data)
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        while current.next and current.next.data != node:
            current = current.next
        if current.next is None:
            print("Cannot insert, "+node+" does not exist.")
            return
        new_node = DataNode(data)
        new_node.next = current.next
        current.next = new_node

    def delete(self,data):
        if not self.head:
           return print("Cannot delete, "+data+" does not exist.")
        
        if self.head.data == data:
            self.head = self.head.next
            self.count -= 1
            return
        
        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next is None:
            print("Cannot delete, "+data+" does not exist.")
            return
        
        current.next = current.next.next
        self.count -= 1
        
    def traverse(self):
        current = self.head
        result = ""
        while current:
            result += current.data
            if current.next:
                result += " -> "
            current = current.next
        if not result:
            result = "This is an empty list."
        return print(result)

def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    text = input()
    condition, data = text.split(": ")
    if condition == "F":
      mylist.insert_front(data)
    elif condition == "L":
      mylist.insert_last(data)
    elif condition == "B":
      mylist.insert_before(*data.split(", "))
    elif condition == "D":
      mylist.delete(data)
    else:
      print("Invalid Condition!")
  mylist.traverse()

main()