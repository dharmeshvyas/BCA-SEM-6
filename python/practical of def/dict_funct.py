def print_key():
    print("the value")

test_dict={"first":print_key,"old":5,"help":"no"}

print("the original dictionary  :",test_dict)

res= test_dict['first']()
print("the requierd call result :",res)
