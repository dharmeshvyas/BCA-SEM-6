#in list is similer to Array and it is mmutable datatype 
#the difference between list and array is the list not need a spacific datatype while inserting the value and array need to spacif datatyp
 
l =[1,"Apple",4,440.1] #decleare the list using []
print(l)

#we can edit the value in list data type
l[2]="ball"
print(l)

#accessing list
print(l[1])

#multiple list
l2 = [[1,3,4,"five"],[1.1,"two",3.1]]
print(l2)

#accessing multi list
print(l2[0][2])
print(l2[1][2])

#limited acceess
for i in l2:
    print(i[0:2])




