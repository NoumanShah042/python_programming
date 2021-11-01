"""
Use of Python static method:

Static methods are formed in a class so that only the class instances can access them.
We can use a static method for simple functionality that is mostly not related to the class.

static method, we do not need the self or cls to be passed as the first argument.
Static methods do not have any knowledge related to the class that they are built-in.
Static method cannot alter or change any variable value or state of the class.

Most of the functionalities of the static methods can be performed using a class method. However, we prefer
the static method, at places where it could work to make our program more efficient and faster
as we do not have to pass self as a parameter, so the efficiency of the program increases.
"""


class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def mark_attendance(string):
        print("This is good " + string)


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")

harry.mark_attendance("Present")
Employee.mark_attendance("Present")

# staticmethod(Employee.mark_attendance("present"))
