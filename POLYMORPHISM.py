#INHERITANCE WITH POLYMORPHISM:POLYMORPHISM means one instance/method has many forms.
# Ex: speak() method used many times under different classes 
#super(): Used to call the constructor method of parent class. 
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
    
    def speak(self):
        return f"{self.name} meows"
    
tommy = dog("Tommy", "xyz")
print(tommy.speak())
mufasa = cat("Mufasa", "white")
print(mufasa.speak())