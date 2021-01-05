''' 
A package is defined by creating a directory. Then you can
place the module source file under that directory. In order for Python 
to know it as Python-package, just create a __init__.py file in this directory. 
'''
from math_stuff import subtract     # from package import module
result = subtract.subtract(5, 1)   # to call function from module use dot notation
print(result)


'''
You can do it slightly different: first import a package.module, then call a function
'''
from math_stuff.subtract import subtract     # from package/module import function
result = subtract(34, 1)   # calling function to use
print(result)




