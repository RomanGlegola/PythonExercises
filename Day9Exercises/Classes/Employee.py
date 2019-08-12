"""klasa"""
class Employee(object):
    """Tworzymy konstruktor"""
    def __init__(self, imie, nazwisko='Kowalski', salary=0):
        self.name = imie
        self.surname = nazwisko
        self.salary = float(salary)

    def say_hello(self):
        print(f'Hello, my name is {self.name} {self.surname}')

    def increase_salary(self, percentage):
        self.salary = (1+percentage/100)*self.salary
    def chceck_salary(self):
        print(f"{self.name} {self.surname} {self.salary}")


new_employee = Employee('Mateusz', 'Cebula', 0)
new_employee.say_hello()
object_instance = Employee('Jan')
object_instance.say_hello()


