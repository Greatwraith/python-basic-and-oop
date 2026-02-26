class Student:
    # Constructor: runs when a new Student object is created
    def __init__(self, name, age):
        self.name = name      # stores attributes(student name and age)
        self.age = age        
        
    
    @staticmethod
    def printStatement(): # # Static method: does NOT use self or cls
        print("this is a static method") # Just a normal function inside the class
        
# Create a Student object
student1 = Student('Ardhan', 17)
print(student1.__dict__)   

# Calling the static method using the object
student1.printStatement()  # works even though it doesn't use object data