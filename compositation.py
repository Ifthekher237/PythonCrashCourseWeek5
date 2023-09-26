# this program shows how composition is used....

class Salary:
    """finds the total salary of an employee after a year"""
    def __init__(self, pay, bonus):
        """this is constructor"""
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        """figures out the total salary"""
        return (self.pay*12) + self.bonus

class Employee:
    """employees information"""
    def __init__(self, name, age, pay, bonus):
        """the constructor"""
        self.name =name
        self.age = age
        self.obj_salary = Salary(pay, bonus)

    def total_salary(self):
        """total salary of an employee"""
        return self.obj_salary.annual_salary()

employee = Employee("Anis", 23, 15000, 10000)
print(employee.total_salary())
