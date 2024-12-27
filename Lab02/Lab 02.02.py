class ArrayStack:
    def __init__(self,):
        self.size = 0
        self.data = list()
    def push(self, input_data):
        """push"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1
    def pop(self):
        """pop"""
        if self.data :
            x = self.data.pop(-1)
            self.size -= 1
            return x
        else :
            print("Underflow: Cannot pop data from an empty list")
            return None
    def is_empty(self):
        """is_empty"""
        if self.data :
            return False
        else :
            return True
    def get_stack_top(self):
        """get_stack_top"""
        if self.data :
            x = self.data.pop(-1)
            self.data.append(x)
            return x
        else :
            print("Underflow: Cannot get stack top from an empty list")
            return None
    def get_size(self):
        """get_size"""
        return self.size
    def print_stack(self):
        """print_stack"""
        return print(self.data)
    
def main():
    """main"""
    students = ArrayStack()
    groups = ArrayStack()
    groups_num = int(input())
    students_num = int(input())
    for _ in range(groups_num):
        groups.push(ArrayStack())
    for _ in range(students_num):
        students.push(input())
    while not students.is_empty():
        temp = ArrayStack()
        while not groups.is_empty() and not students.is_empty():
            group = groups.pop()
            group.push(students.pop())
            temp.push(group)
        while not temp.is_empty():
            groups.push(temp.pop())
    i = 1
    while not groups.is_empty():
        print_group(groups.pop(), i)
        i += 1
def print_group(group : ArrayStack, i : int):
    """print"""
    print(f"Group {i}: ", end="")
    print(*group.data, sep=", ")

main()