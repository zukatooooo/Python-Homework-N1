class School:
    def __init__(self, school_name, school_address):
        self.school_name = school_name
        self.school_address = school_address
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        if index < len(self.students):
            del self.students[index]
        else:
            print("No student found.")

    def show_students(self):
        for student in self.students:
            student.get_info()
