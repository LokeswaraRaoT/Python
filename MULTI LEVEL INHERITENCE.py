#MULTI LEVEL INHERITENCE : Inherit more than one class into single class along with their all the functions.
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