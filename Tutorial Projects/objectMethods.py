#Static Method

class Employee:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
    
    def get_info(self):
        return f"{self.name}: {self.pos}"
        
    # static method - belongs to the class not other objects in the class - best if you dont need access to class data
    @staticmethod
    def is_valid_pos(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions


employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

# # employee = blabla - no need
# print(Employee.is_valid_pos("NASA"))
# print(employee2.get_info())

#Class Methods

class Student: 
    
    count = 0
    total_gpa = 0
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    
    #Instance Method
    def get_info(self):
        return f"{self.name}: {self.gpa}"
    
    #class method - best for class-level data or need access to the class itself
    @classmethod
    def get_count(cls):
        return f"Total # of Students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"
    
student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.2)
student3 = Student("Sandy", 4.0)


# print(Student.get_count())
# print(Student.get_average_gpa())

#Magic Methods or dunder methods(double underscore):

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title 
        self.author = author
        self.num_pages = num_pages
        
    #Changing the string representation(for printing etc)
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    #Changing the equal representation(for checking on other objects)
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    #Changing the lower than(<) representation
    def __lt__(self, other):
        return self.num_pages < other.num_pages

    #Changing the greater than(>) representation
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    #Changing add(+) representation
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    #Changing the contain(in) representation
    def __contains__(self, keyword):
        return keyword in self.title
    
    #Changing the dict get item(['...']) representation
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"Key '{key}' was not found!"
        

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, The Witch, and The Audacity of This Bitch", "C.S. Gaming", 172)
book4 = Book("The Lion, The Witch, and The Audacity of This Bitch", "C.S. Gaming", 169)

# print(book3 == book4)
# print(book3 < book4)
# print(book3 > book4)
# print(book1 + book2)
# print("Lion" in book3)
print(book1['audio'])