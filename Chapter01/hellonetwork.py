''' A package is defined by creating a directory. Then you can
place the module source file under that directory. In order for Python 
to know it as Python-package, just create a __init__.py file in this directory. 
'''
from math_stuff import subtract     # from package import module
result = subtract.subtract(5, 1)   # to call function from module use dot notation
print(result)
print('hello network!')


