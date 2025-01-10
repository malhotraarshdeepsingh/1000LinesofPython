from abc import ABC, abstractmethod  
class Employee:
    # Encapsulation: Private attributes
    def __init__(self, emp_id, name, position, salary):
        self.__emp_id = emp_id  # Private attribute
        self.name = name  
        self.position = position
        self.salary = salary

    def get_emp_id(self):
        return self.__emp_id

    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def display_details(self):
        return f"ID: {self.__emp_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, emp_id, name, position, salary, department):
        super().__init__(emp_id, name, position, salary)
        self.department = department

    def display_details(self):
        return f"{super().display_details()}, Department: {self.department}"

class TaskManagement(ABC):
    @abstractmethod
    def assign_task(self, task, emp_id):
        pass

    @abstractmethod
    def view_tasks(self, emp_id):
        pass

class Utils:
    @staticmethod
    def validate_salary(salary):
        return salary > 0
    
class TaskSystem(TaskManagement):
    def __init__(self):
        self.tasks = {} 

    def assign_task(self, task, emp_id):
        if emp_id not in self.tasks:
            self.tasks[emp_id] = []
        self.tasks[emp_id].append(task)

    def view_tasks(self, emp_id):
        return self.tasks.get(emp_id, [])

class Developer(Employee):
    def __init__(self, emp_id, name, position, salary, programming_language):
        super().__init__(emp_id, name, position, salary)
        self.programming_language = programming_language

    def display_details(self):
        return f"{super().display_details()}, Programming Language: {self.programming_language}"


if __name__ == "__main__":
    # Creating employees
    emp1 = Employee(101, "John Doe", "Intern", 30000)
    emp2 = Manager(102, "Jane Smith", "Manager", 60000, "Finance")
    emp3 = Developer(103, "Alice Johnson", "Developer", 50000, "Python")

    # Displaying details
    print(emp1.display_details())
    print(emp2.display_details())
    print(emp3.display_details())

    # Using TaskSystem
    task_system = TaskSystem()
    task_system.assign_task("Prepare financial report", 102)
    task_system.assign_task("Develop API", 103)

    print(f"Tasks for {emp2.name}: {task_system.view_tasks(102)}")
    print(f"Tasks for {emp3.name}: {task_system.view_tasks(103)}")

    # Demonstrating static method
    print("Is salary valid:", Utils.validate_salary(emp1.salary))
