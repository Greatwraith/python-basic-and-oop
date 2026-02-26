class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    def result(self):
        if self.grade >= 500:
            return "Congratulaion, You PASS the test! ✅"
        else:
            return "Sorry, You Fail the test. don't worry, take this as your experience! "
        
student1 = Student('Ardhan', 501)

print(student1.result())     