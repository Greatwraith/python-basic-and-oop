class Student: # creating a class name 'Student'
    def __init__(self, name,roll_num,age ): 
        # this will act as blueprint
        self.name = name
        self.roll_num = roll_num
        self.StudentAge = age
        # self.XxX doesn't have to be as exact same as just 'age'
    
# defining a constructor __init__.
# __init__ is a constructor, which Sets up object data (name, roll number, age)
# (self) is an Object Parameter

# Parameter is used to talk about the behavior of the next object,
# which you want to create in your class, 
# helps you to tell the class what attribute and what methods you want in your class. 






student1 = Student('John doe', 54325, 20)
student2 = Student("Ardhan", 543254, 17)

student1.name # use to take the student1's name
student1.roll_num # use to take the student1's roll number
student1.StudentAge # use to take the student1's StudentAge

print(student1)
print(student1.name) 
print(student1.roll_num)
print(student1.StudentAge)


print(student2)
print(student2.name) 
print(student2.roll_num)
print(student2.StudentAge)




        
        
        

        
        
    
