class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def result(self):
        if self.marks >= 500:
            return "pass"
        else:
            return "fail"

s1 = Student('Ardhan',17,500)
s2 = Student('thanos', 39, 394)
s3 =Student('deadpool', 20, 430)
s4 = Student('venom', 33, 670)
s5 =Student('superman', 25, 555)
s6 =Student('Bruce wayne', 22, 493)


student_objects = [s1,s2,s3,s4,s5,s6]

passStudents = []
failStudents = []
student_results= {}

for student in student_objects:
    if student.result() == 'pass':
        passStudents.append(student.name)
        student_results['pass students'] = passStudents
    else:
        failStudents.append(student.name)
        student_results['fail students'] = failStudents
        
        
print(student_results)