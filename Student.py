class Student:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def get_info(self):
        print(f"{self.firstname} {self.lastname}")
