#Polymorphism

#Inheritence
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
        

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("Pepperoni", 15)]

# for shape in shapes:
#     print(f"{shape.area()} cm^2")
    
#Duck Typing
class Animal:
    alive = True
    
class Dog(Animal):
    def speak(self):
        print("WOOF!")
        
class Cat(Animal):
    def speak(self):
        print("MEOW!")

#Clearly not similar
class Car:
    alive = False
    
    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()