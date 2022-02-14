my_dict = {'name': 'dharmesh', 'age': 20}

print("\nInitial dictionary :",my_dict)
#update dictionary
my_dict['age']=21
print("\nupdate key value :",my_dict)

#add value and key in exsiting
my_dict['address']="shapar"

print("\nAdd Key :",my_dict)
#delete key
del my_dict['name']
print("\nAfter delete :",my_dict)

#clear dictionary

my_dict.clear()
print("\nafter clear dict :",my_dict)
