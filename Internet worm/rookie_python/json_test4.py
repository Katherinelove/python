import json

class Classroom():
    def __init__(self,roomnumber,students=[]):
        self.roomnumber=roomnumber
        self.students=students
    def get_json_dict(self):
        d = vars(self)
        student_list = []
        for student in self.students:
            student_list.append(vars(student))
        d["students"] = student_list
        return d

class Student():
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade


hongliu=Student("hongliu",100)
zengshuai=Student("zengshuai",100)
first_grade=Classroom("d418",[hongliu,zengshuai])

print(vars(zengshuai))
print(vars(first_grade))

print(vars(zengshuai))
print(first_grade.get_json_dict())