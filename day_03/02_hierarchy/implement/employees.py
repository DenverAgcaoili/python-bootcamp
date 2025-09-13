class Employee:
    """Class representation for employee data"""

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created with ID {self.id}")

    def add_work(self, task):
        print(f"Added work to {self.name}: {task} ")
        return self.tasks.append(task)


class Recruiter(Employee):

    def set_initial_interview(self, candidate):
        self.add_work(f"Interview {candidate}")

class Developer(Employee):
    def code(self):
        self.add_work("code")



class Manager(Employee):
    def set_one_on_one(self,subordinate):
        self.add_work(f"Send invite to {subordinate}")



dev_1 = Developer("Jeff", 123)
dev_1.add_work("refactor")

manager_1 = Manager("Bob", 456)
manager_1.set_one_on_one("Jeff")