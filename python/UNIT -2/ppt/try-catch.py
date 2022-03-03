try:
    print("try block")
    x = int(input("Enter a Number :"))
    y = int(input("Enter another Number :"))
    z=x/y
except ZeroDivisionError:
    print("except zero division error block")
    print("division by 0 no accepted")
else:
    print("else block")
    print("division =",z)
finally:
    print("finally block")
    x=0
    y=0
    print("out of try,except ,else and finally block")
