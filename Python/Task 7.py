from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name):
        self.name=name
        
    
    @abstractmethod
    def get_salary():
        pass
    
class FixedEmployee(Employee):
    def __init__(self,name,monthly_salary):
        super().__init__(name)
        self.monthly_salary=monthly_salary
    
    def get_salary(self):
        return self.monthly_salary

class HourlyEmployee(Employee):
    def __init__(self,name,hourly_rate,hours_worked):
        super().__init__(name)
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked

    def get_salary(self):
        return self.hourly_rate*self.hours_worked
    
fixed_emp=FixedEmployee("Alice",5000)
hourly_emp=HourlyEmployee("Bob",20,160)

print(f"{fixed_emp.name}'s salary is {fixed_emp.get_salary()}")
print(f"{hourly_emp.name}'s salary is {hourly_emp.get_salary()}")
    

