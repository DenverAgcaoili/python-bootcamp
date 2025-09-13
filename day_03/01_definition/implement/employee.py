class Employee:
    def __init__(self,name, id):
        self.name = name
        self.id =id
        self.task =[]
        print(f"Employee {name} created with id {id}")

    def add_task(self,task):
        print(f"Adding task {task} to {self.name}")
        self.task.append(task)

employee1 = Employee("Richard",123)
employee2 = Employee("Jelly",456)


print (employee1.name)