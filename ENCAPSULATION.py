# ENCAPSULATION : Encapsulation means hiding the internal utils. 
# We can achieve an encapsulation by making a method, variable, attribute inside the class as a private variable.
# Hiding the internal data to exposing outside.
# Private variable: double under score (__) used to define variable, functions or methods explicitly. 
# we cannot able to directly access it Outside of the class. We can access it at out side to declare one more function in the class and call that function only.
class employee():
    __bonus = 10000 #----> Private Variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def emp_details(self):
        return f"{self.name} belonging to employee class"
    
    def emp_salary(self):
        return f"{self.name} salary is : {self.salary}"
    
    def __emp_salary_with_bonus(self): ## this private class can not assess it directly outside of the class
        return f"{self.name} salary with bonus is : {self.salary + self.__bonus}"
    
    # if we want to access it outside of the class declare one more function
    def sal_details(self): #declare one more function in the class and call that function only.
        return self.__emp_salary_with_bonus() #
    

cls_ins = employee("Lokesh", 25000)

#print(cls_ins.emp_salary())
print(cls_ins.sal_details())

