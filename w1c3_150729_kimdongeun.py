ass Student(object):
    def __init__(self, number, name):
        self.number = number
        self.name = name


#출석부
attendances = {}


def call(object):
    if isinstance(object, Student):
        attendances[object.number] = object

def print_attendances():
    for student in attendances.values():
        print("%d : %s" % (student.number, student.name))

student_1 = Student(1,'dongeun')
student_2 = Student(2,'kyeongmook')
student_3 = Student(3,'jinsuk')

call(student_1)
call(student_2)
call(student_3)

print_attendances()

