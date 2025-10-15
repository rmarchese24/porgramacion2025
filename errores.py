a = 2
b = 0
try:
    c = a / b
except ZeroDivisionError:
    print ("NO puede realizar la operacion ")
    

a = 2
b = 0
try:
    c = a / b
except Exception as error:
    print ("NO puede realizar la operacion " , type(error))