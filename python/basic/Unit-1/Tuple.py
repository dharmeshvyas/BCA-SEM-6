#tuple is like list and other ordered collection of object
#tuple are immutable data type ,means it can not change after declaration

#decleare tuple using () 
tp =(0,"Zip",3.14)

#print a tuple
print(tp)

#print a spacific value from tuple
print(tp[2])

#decleare tuple using tuple()
p2= tuple("tuple")
print(p2)       #it split the String

#tuple are immutable      ,it just try catch like java now it not require to learn 
try:
    tp[0]=1;#it creating error
except Exception as error:
    
    print(error)
    
#accesse value using slice operator
    print(tp[0:2])
     
#store multiple list in tuple
l1=[1,2,3,4,5,6]
l2=["one","two","three","four"]
mtp=(l1,l2)
print(mtp)

#create nasted tuple
tuple1=tuple("Start")
tuple2=(4,67,4)
tuple3=(tuple1,tuple2)
print(tuple3)
