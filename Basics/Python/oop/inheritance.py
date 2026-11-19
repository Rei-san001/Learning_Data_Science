# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
        
        
        
# class Student(Person):
#     def study(self):
#         print(f"{self.name} is studying.")
   

# s1 = Student("Alice", 20)
# s1.greet()
# s1.study()

# p1  = Person("Alan", 25)
# p1.greet()




# SINGLE INHERITANCE (ONE PARENT, ONE CHILD)

# class Animal:
#     def eat(self):
#         print("This animal eats rice")


# class Dog(Animal):
#     def bark(self):
#         print("woof!")
        
# d = Dog()
# d.bark()
# d.eat()




# MULTI LEVEL INHERITANCE (GRAND PARENT, PARENT, CHILD)


# class Animal:
#     def eat(self):
#         print("This animal eats rice")


# class Dog(Animal):
#     def bark(self):
#         print("woof!")
        
# class Puppy(Dog):
#     def weep(self):
#         print("weeping")



# d = Dog()
# d.bark()
# d.eat()

# p = Puppy()
# p.eat()
# p.bark()
# p.weep()


# HIERARCHICAL INHERITANCE (ONE PARENT, SOME CHILD)

# class Animal:
#     def eat(self):
#         print("This animal eats rice")


# class Dog(Animal):
#     def bark(self):
#         print("woof!")

# class Cat(Animal):
#     def meow(self):
#         print("Meowing")
        
        
# d = Dog()
# c = Cat()

# d.eat()
# d.bark()


# c.eat()
# c.meow()


#MULTIPLE INHERITANCE (ONE CHILD, MANY PARENTS)

class Father:
    def skills(self):
        print("Gardening, Cooking")

class Mother:
    def hobbies(self):
        print("Painting, Music")
        
class Child(Father, Mother):
    def own(self):
        print("coding")
        
c = Child()
c.own()
c.skills()
c.hobbies()