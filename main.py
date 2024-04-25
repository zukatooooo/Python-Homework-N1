from School import School
from Student import Student

school = School("Newton Free School", "Politkovskaiyas 30a")

student1 = Student("Alice", "Smith", 15)
student2 = Student("Bob", "Johnson", 16)
student3 = Student("Charlie", "Brown", 17)

school.add_student(student1)
school.add_student(student2)
school.add_student(student3)

school.show_students()
