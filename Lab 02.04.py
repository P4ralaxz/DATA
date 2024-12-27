class ArrayStack:
    def __init__(self,):
        self.data = list()
        self.err = 0
    def push(self, input_data):
        """push"""
        self.data.append(input_data)
    def pop(self):
        """pop"""
        if self.data :
            x = self.data.pop()
            return x
        else :
            print("Underflow: Cannot pop data from an empty list")
            self.err += 1
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
            x = self.data.pop()
            self.data.append(x)
            return x
        else :
            print("Underflow: Cannot get stack top from an empty list")
            return None
    def print_stack(self):
        """print_stack"""
        return print(self.data)
    def empty(self):
        self.data.clear()

def main():
    """main"""
    arr =  ArrayStack()
    x = input()
    for i in x:
            if i == '(':
                arr.push(i)
            elif i == ')':
                arr.pop()
    if arr.is_empty() and arr.err == 0:
        print(f"Parentheses in {x} are matched")
        print("True")
    else:
        print(f"Parentheses in {x} are unmatched")
        print("False")
main()