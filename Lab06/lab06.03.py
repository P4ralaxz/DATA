class Student:
    def __init__(self,id,name,gpa):
        self.id = id
        self.name = name
        self.gpa = gpa
        
    def get_std_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_gpa(self):
        return f"{self.gpa:.2f}"
    
    def print_details(self) :
        print("ID:", self.get_std_id())
        print("Name:", self.get_name())
        print("GPA:", self.get_gpa())

def Binary_search(data, name):
    left = 0
    right = len(data) - 1
    compar = 0

    while left <= right:
        mid = (left + right) // 2
        compar += 1

        if data[mid].name == name:
            print(f"Found {name} at index {mid}")
            data[mid].print_details()
            print("Comparisons times:", compar)
            return
        elif data[mid].name < name:
            left = mid + 1
        else:
            right = mid - 1

    print(f"{name} does not exists.")
    print("Comparisons times:", compar)


def main(text_in):
    import json
    std_in = json.loads(text_in)
    students = [Student(s["id"], s["name"], s["gpa"]) for s in std_in]

    search_name = input().strip()

    Binary_search(students, search_name)
main(input())