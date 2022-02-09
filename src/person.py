# coding: utf-8

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age


class Student(Person):
    def __init__(self, school, name, age) -> None:
        super().__init__(name, age)
        self.school = school
    
    def grade(self, n):
        print("{0}'s grad is {1}".format(self.name, str(n)))


stu1 = Student("Soochow", "Galieo", 27)
stu1.grade(99)