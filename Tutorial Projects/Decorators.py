#Decorator = function that extends behavior of another function

def add_sprinkles(func):
    #Wrapper is so that we add the decorator only when we call the get_ice_cream function. *args & **kwargs to be able to accept any number of arguments.
    def wrapper(*args, **kwargs):
        print("*You add sprinkles 🎊*")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge 🍫*")
        func(*args, **kwargs)
    return wrapper

#Decorators
@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍦")

get_ice_cream("Vanilla")




# @property = Decorator
# Benefit: add additional logic when read, write, or delete attributes

class Rectangle:
    def __init__(self, width, height):
        #._ means the attributes using that are meant to be protected because they are internal, so they shouldn't be accessed those attributes directly outside of the class
        self._width = width
        self._height = height
        
    #Getter Methods
    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    #Setter Methods
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")
        
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")
            
    #Deleter Methods
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted!")
        
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted!")
        
        
rectangle = Rectangle(3,4)

# del rectangle.width
# print(rectangle.width)
# print(rectangle.height)