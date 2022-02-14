#Data type in python

#python has dynamic data type ,it means it automatically change variable get type of value
int1=12
flt = 12.55
str1 = "Name of something"
com = 1+5j
#type() is used to check the stored value's data type

print("Syntex : type(variable)",)
print("\n\nlist of datatypes")
print("datatype :",type(int1),"\tValue :",int1)
print("datatype :",type(flt),"\tValue :",flt)
print("datatype :",type(str1),"\tValue :",str1)
print("datatype :",type(com),"\tValue :",com)

#isinstance() is used to the variable of object is belong to perticuler data type of class and it return true or false

#Syntex : isinstance(variable ,datatype)

print("is variable 'flt' is belongs to float(class) or not :",isinstance(flt,float))



