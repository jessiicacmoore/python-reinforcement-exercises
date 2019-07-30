class Task:

    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date

    def __repr__(self):
        return f"{self.description} by {self.due_date}"


class ToDoList:
   
    def __init__(self, name):
        self.name = name
        self.to_dos = []

    def add_task(self, task):
        self.to_dos.append(task)


task1 = Task('Clean the kitchen', 'This Friday')
task2 = Task('Buy Groceries for the week', 'This Sunday')
task3 = Task('Pay credit card bill', 'Next Wednesday')

personal_tasks = ToDoList('Personal Tasks')


print(personal_tasks.to_dos)  # []
personal_tasks.add_task(task1)
print(personal_tasks.to_dos)  # [Clean the kitchen by This Friday]
personal_tasks.add_task(task2)
print(personal_tasks.to_dos)  # [Clean the kitchen by This Friday, Buy Groceries for the week by This Sunday]
personal_tasks.add_task(task3)
print(personal_tasks.to_dos)  #  [Clean the kitchen by This Friday, Buy Groceries for the week by This Sunday, Pay credit card bill by Next Wednesday]





