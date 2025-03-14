# Import the functions and classes form the Utility file
from  UTILS import (
    addition, 
    greet, 
    multiplication,
    sample_cls
)

print(greet())
print(addition(10, 20))
print(multiplication(10, 20))

s =sample_cls()
print(s.get_cls_details())



