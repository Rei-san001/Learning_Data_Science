class Student:
    def __init__(self, namee, cgpaa): #constructor 
        self.name = namee # self means in simple terms "this" in other programming languages
        self.cgpa = cgpaa
        
        #self is a reference 
        # Attaches 'namee' to this specific instance
        
    def show_info(self):
        print(f"Name: {self.name}, CGPA: {self.cgpa}")

s1 = Student("Rei", 3.5)

print(type(s1))
print(s1.name)
s1.show_info()

