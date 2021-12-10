a = int( input("Please Enter first number a: "))
b= int(input("Please Enter Second number b: "))
c= input("Please choose your arithmetic operator[+ - * /]: ")
result=0
if c=="+":
    result= a + b
    print("the result of  of a + b is = " ,result)
elif c=="-":
    result= a -b
    print("the result of of a - b is = " ,result)
elif c=="*":
    result = a*b
    print("the result of of a  b is = ",result)
elif c =="/":
    result = a / b
    print("the result of  a / b is = " ,result)
else:
    print("this opeator is not available")
    print (a,c,b,"=", result)