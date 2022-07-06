students = [("Allen Anderson", "Computer Science"),
            ("Edgar Einstein", "Engineering"),
            ("Farrah Finn", "Fine Arts")]
    
def add_new_student(students, name, major):
    students.append((name, major))

def update_student(students, index, name, major):
    students[index] = (name, major)

def find_students_by_name(students, name):
    return [student for student in students if name in student[0]]

def get_all_majors(students):
    return [student[1] for student in students]

find_students_by_name(students, 'in')
get_all_majors(students)


int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

import random
print(random.randint(2,5))

print("Hello", 42)
print("Hello " + str(42))

def help(x):
    return x % 2 == 0

int(help(2))

2//3