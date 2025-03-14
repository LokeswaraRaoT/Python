#CONSTRUCTOR METHOD: It is always __init__(double under score init double under score)
#Example1:
				
class calculate():
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2
    
    def sub(self, num1, num2):
        return num1 - num2
    
    def mul(self, num1, num2):
        return num1 * num2

calc_instance = calculate()

print(calc_instance.add(10, 30))
print(calc_instance.sub(30, 10))
print(calc_instance.mul(30, 20))


#Example2:

class calculator():
    def __init__ (self, num1, num2): #self represents to any method is related to the calss
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
            return self.num1 + self.num2
    def sub(self):
            return self.num1 - self.num2
    def multi(self):
            return self.num1 * self.num2
    def div(self):
            return self.num1 // self.num2

first_instance  = calculator(10, 20) # We have to call these methods inside this class “calculator” by using this instance object”first_instance”.
print(first_instance.add())
print(first_instance.sub())
print(first_instance.multi())

#Example3:

class employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_emp_name(self):
            return f"{self.name} is belongs to employee"
        
    def get_emp_salary(self):
            return f"{self.name} salary is : {self.salary}"
           
cls_name = employee("Lokesh", 30000)

print(cls_name.get_emp_salary()) #call the function with class



