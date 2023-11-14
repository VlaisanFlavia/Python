class Employee:
    def __init__(self, name, employee_id, title):
        self.name = name
        self.employee_id = employee_id
        self.title = title

    def display_info(self):
        return f"{self.title}: {self.name}, ID: {self.employee_id}"


class Manager(Employee):
    def __init__(self, name, employee_id, department, salary):
        super().__init__(name, employee_id, title="Manager")
        self.department = department
        self.salary = salary

    def display_info(self):
        return f"{super().display_info()}, Department: {self.department}, Salary: ${self.salary}"

    def organize_meeting(self):
        return f"{self.name} is organizing a meeting."


class Engineer(Employee):
    def __init__(self, name, employee_id, programming_language, salary):
        super().__init__(name, employee_id, title="Engineer")
        self.programming_language = programming_language
        self.salary = salary

    def display_info(self):
        return f"{super().display_info()}, Programming Language: {self.programming_language}, Salary: ${self.salary}"

    def write_code(self):
        return f"{self.name} is writing code."


class Salesperson(Employee):
    def __init__(self, name, employee_id, territory, salary, commission_rate):
        super().__init__(name, employee_id, title="Salesperson")
        self.territory = territory
        self.salary = salary
        self.commission_rate = commission_rate

    def display_info(self):
        return f"{super().display_info()}, Territory: {self.territory}, Salary: ${self.salary}, Commission Rate: {self.commission_rate}%"

    def make_sale(self):
        return f"{self.name} made a sale."


manager = Manager(name="John Smith", employee_id=101, department="HR", salary=70000)
print(manager.display_info())
print(manager.organize_meeting())

engineer = Engineer(name="Alice Johnson", employee_id=102, programming_language="Python", salary=90000)
print(engineer.display_info())
print(engineer.write_code())

salesperson = Salesperson(name="Bob Davis", employee_id=103, territory="North America", salary=60000, commission_rate=5)
print(salesperson.display_info())
print(salesperson.make_sale())
