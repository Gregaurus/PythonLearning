
#Class
class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    def drive(self):
        print(f"You drive the {self.color} {self.model}")
    
    def stop(self):
        print(f"You stopped the {self.color} {self.model}")
    
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
        
#Class Variables
class Student:
    
    student_year = "2024"
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

#Class Inheritence - Good to write efficient code for recurring attributes/methods
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEAK!")
        
#Multiple Inheritance & Multilevel Inheritance
class Prey(Animal):
    def flee(self):
        print("This animal is fleeing!")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting!")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Predator, Prey):
    pass

#Super()

class Shape():
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
    
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius
        
    #Method overwriting(child first before parent for similar methods)
    def describe(self):
        super().describe()
        print(f"it is a circle with an area of {3.14 * self.radius * self.radius} cm^2")

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height


car1 = Car("Lamborghini", "1994", "Silver", False)
car2 = Car("Mustang", "2000", "Blue", False)
# car2.drive()
# car1.stop()
# car1.describe()

student1 = Student("Rego", "24")
student2 = Student("Bobi", "23")
student2 = Student("Alisha", "23")

# print(student1.name)
# print(student1.age)
# print(Student.student_year)
# print(Student.num_students)
print(f"My Graduating class of {Student.student_year} has {Student.num_students} students")

dog = Dog("Powie")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

# print(dog.name)
# mouse.speak()

rabbit = Rabbit("Harry")
hawk = Hawk("Potter")
fish = Fish("Patrick")

# hawk.sleep()

circle = Circle(color= "red", filled= True, radius= 5)
circle.describe()



