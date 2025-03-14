# PARENT -----> FUNCTIONS -----> CHILD
class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes sound"
    
dog = Animal("Tommy")
print(dog.speak())
