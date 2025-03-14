param1 = 12
param2 = 23

#class employee:
 #   def __init__(self, name, salary):  # Fixed __init__
  #      self.name = name
   #     self.salary = salary

#    def get_emp_details(self):
 #       return f"{self.name} belongs to employee class"
    
  #  def get_emp_salary(self):
   #     return f"{self.name} salary is : {self.salary}"

# Create an instance of the employee class
#my_cls_ins = employee("Lokesh", 20000)

# Call the method using the instance
#print(my_cls_ins.get_emp_salary())  # Corrected to use instance
#class calculate():
    
 #   def __init__(self):
        ##pass

  #  def add(self, num1, num2):
        #return num1 + num2
    
    #def sub(self, num1, num2):
     #   return num1 - num2
    
   # def mul(self, num1, num2):
    #    return num1 * num2

#calc_instance = calculate()

#print(calc_instance.add(10, 30))
#print(calc_instance.sub(30, 10))
#print(calc_instance.mul(30, 20))
class employee():
    __bonus = 10000

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def emp_details(self):
        return f"{self.name} belonging to employee class"
    
    def emp_salary(self):
        return f"{self.name} salary is : {self.salary}"
    
    def __emp_salary_with_bonus(self):
        return f"{self.name} salary with bonus is : {self.salary + self.__bonus}"
    
    def sal_details(self):
        return self.__emp_salary_with_bonus()
    

cls_ins = employee("Lokesh", 25000)

#print(cls_ins.emp_salary())
print(cls_ins.sal_details())

class Animal():
    __private_var = "xyz"
    normal_var = "zyx"
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes sound"
    
dog = Animal("Tommy")
print(dog.speak())

cat = Animal("Mufasa")
print(cat.speak())

class ParentClass():
    def get_details_of_parent(self):
        return f"I am the parent class"
    
class ChildClass1():
    def get_details_of_child1(self):
        return f"I am the child class"
    
class ChildClass2(ParentClass, ChildClass1):
    def get_details_of_child2(self):
        return f"I am the child class2"
    
child_cls_instance = ChildClass2()
print(child_cls_instance.get_details_of_parent())
print(child_cls_instance.get_details_of_child1())
print(child_cls_instance.get_details_of_child2())

class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes sound"
    
class dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        return f"{self.name} barks"
    
class cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    #def speak(self):
       # return f"{self.name} meows"
    
tommy = dog("Tommy", "xyz")
print(tommy.speak())
mufasa = cat("Mufasa", "white")
print(mufasa.speak())




    

