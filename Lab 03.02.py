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
    mylist.insert_last(input())
  mylist.traverse()

main()