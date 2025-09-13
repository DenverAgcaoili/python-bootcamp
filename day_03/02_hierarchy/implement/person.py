class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        return f"Hi I am {self.first_name} {self.last_name}"


class Student(Person):
        def __init__(self,first_name, last_name, level):
            super().__init__(first_name,last_name)
            self.level = level

        def introduce(self):
            return super().introduce() +  f". I am a student"


student_1 = Student("Jeff", "Castro",12)
print(student_1.introduce())

person_1 = Person("Richard", "Smith")
print(person_1.introduce())