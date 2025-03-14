param1 = 12
param2 = 23

class employee:
    def __init__(self, name, salary):  # Fixed __init__
        self.name = name
        self.salary = salary

    def get_emp_details(self):
        return f"{self.name} belongs to employee class"
    
    def get_emp_salary(self):
        return f"{self.name} salary is : {self.salary}"

# Create an instance of the employee class
my_cls_ins = employee("Lokesh", 20000)

# Call the method using the instance
print(my_cls_ins.get_emp_salary())  # Corrected to use instance