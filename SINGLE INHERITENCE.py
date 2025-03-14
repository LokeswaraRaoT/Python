#SINGLE INHERITENCE : Inherit one class from one single class
class ParentClass():
    def get_details_of_parent(self):
        return f"I am the parent class"
    
class ChildClass(ParentClass):	##Inherit only single class along with functions
    def get_details_of_child(self):
        return f"I am the child class"
    
child_cls_instance = ChildClass()
print(child_cls_instance.get_details_of_child())
print(child_cls_instance.get_details_of_parent())
