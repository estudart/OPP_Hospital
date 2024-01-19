from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name: str, age: int, salary: float, role: str, active: bool, hospital: str):
        self.name = name
        self.age = age
        self.salary = salary
        self.role = role
        self.active = active
        self.hospital = hospital
    
    @abstractmethod
    def __str__(self):
       pass

    @abstractmethod
    def inactive_employee(self):
        pass


class Doctor(Employee):
    def __init__(self, name: str, age: int, salary: float, especialization: str):
        super().__init__(name, age, salary, role="Doctor", active=True, hospital=None)
        self.especialization = especialization

    def __str__(self):
        if self.hospital:
            return f"{self.role} {self.name}, Hopistal: {self.hospital}"
        else:
            return f"{self.name}, Hopistal: Not registered"
    
    def inactive_employee(self):
        self.active = False
        return
    

class Nurse(Employee):
    def __init__(self, name: str, age: int, salary: float, department: str):
        super().__init__(name, age, salary, role="Nurse", active=True, hospital=None)
        self.department = department
    
    def __str__(self):
        if self.hospital:
            return f"{self.name}, Hopistal: {self.hospital} "
        else:
            return f"{self.name}, Hopistal: Not registered"
    
    def inactive_employee(self):
        self.active = False
        return

class Hospital:
    def __init__(self, name: str):
        self.name = name
        self.employees = []
    
    def hire_employee(self, employee):
        employee.hospital = self.name
        self.employees.append(employee.name)
        print(f"{employee.name} hired at {self.name}")

    def get_employees(self):
        return print(f"{self.employees}")

h1 = Hospital('CopaStar')
h2 = Hospital('Miguel Couto')
d1 = Doctor('Enio Studart', 64, 10600.45, 'Pneumology')
d2 = Doctor('Priscila', 50, 2000, 'Ayurveda')
print(d1)
print(d2)
n1 = Nurse('Maria Zelia', 34, 3000.67, 'Brain Cirurgy')
print(n1)
h1.hire_employee(d1)
h1.hire_employee(d2)
print(d1.hospital)
h1.get_employees()
